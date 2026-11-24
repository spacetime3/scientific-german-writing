# -*- coding: utf-8 -*-
"""Vorabscan eines deutschen wissenschaftlichen Textes.

Liefert KANDIDATEN für die Kontextprüfung, keine Urteile:
  * Mustertreffer aus patterns_de.py (mit Prüffrage)
  * Satzstatistik (Längen, Gleichförmigkeit, Satzanfänge, Konnektoren)
  * Nominalstil-Indikatoren (Nominalisierungsdichte, Genitivketten)
  * Dreierreihen, Gedankenstriche, 'Dies'-Satzanfänge ohne Bezugsnomen
  * Redundanzkandidaten (inhaltlich ähnliche Sätze in verschiedenen Absätzen)

Formeln, LaTeX-Befehle, Zitate und Abkürzungen werden vor der Analyse
maskiert, damit sie weder als Satzgrenze noch als Treffer zählen.

Aufruf:
  python scan_text.py text.md                 # Bericht (Text)
  python scan_text.py text.md --json          # maschinenlesbar
  python scan_text.py text.md --min-weight 2  # nur gewichtigere Muster
  type text.md | python scan_text.py -        # von stdin
"""
import argparse
import json
import re
import statistics
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from patterns_de import PATTERNS, CONNECTORS, ABBREVIATIONS  # noqa: E402

for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8")
    except Exception:
        pass

DOT = "\u2024"  # Ersatzpunkt (ONE DOT LEADER) für maskierte Abkürzungen

MATH_RE = re.compile(
    r"\$\$.+?\$\$|\$[^$\n]+?\$|\\\[.+?\\\]|\\\(.+?\\\)|"
    r"\\begin\{(equation|align|eqnarray|gather|multline)\*?\}.+?\\end\{\1\*?\}",
    re.S,
)
LATEX_CMD_RE = re.compile(r"\\(?:cite[pt]?|eqref|ref|autoref|cref|label)\{[^}]*\}")
NOMINAL_RE = re.compile(r"\b[A-ZÄÖÜ][a-zäöüß]+(?:ung|heit|keit|ion|ität|ismus|anz|enz)(?:en|s)?\b")
# Dreistufige Kette mit Nominalisierung am Kopf: "die Prüfung der Sicherheit des Produkts".
# Zweistufige Genitive ("der Dotierung des Faserkerns") sind normales Deutsch und werden nicht gemeldet.
GENITIVE_CHAIN_RE = re.compile(
    r"\b(?i:die|der|des|den|dem|eine|einer|eines)\s+(?:\w+\s+)?[A-ZÄÖÜ]\w+(?:ung|heit|keit|ion|ität)\w*\s+"
    r"(?:der|des|eines|einer)\s+(?:\w+\s+)?[A-ZÄÖÜ]\w+\s+(?:der|des|eines|einer)\s+(?:\w+\s+)?[A-ZÄÖÜ]\w+"
)
TRIPLET_RE = re.compile(
    r"\b([\wäöüÄÖÜß-]+(?:\s+[\wäöüÄÖÜß-]+)?),\s+([\wäöüÄÖÜß-]+(?:\s+[\wäöüÄÖÜß-]+)?)\s+(?:und|sowie|oder)\s+([\wäöüÄÖÜß-]+(?:\s+[\wäöüÄÖÜß-]+)?)\b"
)
DIES_RE = re.compile(r"^(?:Dies|Das|Dieses)\s+(?:ist|sind|war|zeigt|führt|bedeutet|ermöglicht|verdeutlicht|unterstreicht|liegt|hat|wird|kann|lässt|ergibt|erklärt|macht)\b")
CITATION_RE = re.compile(r"\[\s*\d+(?:\s*[,–\-]\s*\d+)*\s*\]|\\cite|\((?:[^()]*?)\b(?:1[89]|20)\d\d[a-z]?\b[^()]*\)|\b[A-ZÄÖÜ]\w+(?: et al\.)? \((?:1[89]|20)\d\d")
WORD_RE = re.compile(r"[A-Za-zÄÖÜäöüß][\wÄÖÜäöüß-]*")

STOPWORDS = set("""
der die das den dem des ein eine einer eines einem einen und oder aber sowie
ist sind war waren wird werden wurde wurden sein kann können muss müssen soll
sollen durch für mit von zu zum zur bei im in an auf aus als auch nicht nur sich
dass wie wenn dann diese dieser dieses diesen diesem es sie er wir man so noch
hier dabei somit damit jedoch zudem werden wobei sehr mehr bzw daher weil dies
""".split())


def mask(text):
    """Formeln/Befehle durch Platzhalter ersetzen, Abkürzungspunkte maskieren."""
    store = []

    def keep(m):
        store.append(m.group(0))
        return f"⟦M{len(store) - 1}⟧"

    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)  # Kommentare ignorieren
    text = re.sub(r"\s*⟨[^⟩]*⟩", "", text)  # Prüfanmerkungen der Skill ignorieren
    t = MATH_RE.sub(keep, text)
    t = LATEX_CMD_RE.sub(keep, t)
    for ab in sorted(ABBREVIATIONS, key=len, reverse=True):
        t = re.sub(r"(?<![\wÄÖÜäöüß])" + re.escape(ab), ab.replace(".", DOT), t)
    # Dezimalzahlen und Ordinalzahlen vor Großbuchstaben nicht als Satzende
    t = re.sub(r"(\d)\.(\d)", r"\1" + DOT + r"\2", t)
    return t, store


def split_paragraphs(text):
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    # Überschriften (Markdown) und reine Formelblöcke auslassen
    out = []
    for p in paras:
        if re.fullmatch(r"#+ .*", p) or re.fullmatch(r"⟦M\d+⟧[\s.,]*", p):
            continue
        out.append(re.sub(r"\s*\n\s*", " ", p))
    return out


def split_sentences(par):
    parts = re.split(r"(?<=[.!?])\s+(?=[A-ZÄÖÜ„\"(\[⟦0-9])", par)
    return [s.strip() for s in parts if s.strip()]


def unmask(s, store):
    s = s.replace(DOT, ".")
    return re.sub(r"⟦M(\d+)⟧", lambda m: store[int(m.group(1))], s)


def words(s):
    return WORD_RE.findall(re.sub(r"⟦M\d+⟧", " FORMEL ", s))


def content_set(s):
    return {w.lower() for w in words(s) if len(w) > 3 and w.lower() not in STOPWORDS and w != "FORMEL"}


def analyse(text, min_weight=1):
    masked, store = mask(text)
    paras = split_paragraphs(masked)
    sentences = []  # (p_idx, s_idx, masked_sentence)
    for pi, p in enumerate(paras, 1):
        for si, s in enumerate(split_sentences(p), 1):
            sentences.append((pi, si, s))

    # Gewichtigere Muster zuerst, damit enthaltene Teiltreffer unterdrückt werden
    compiled = [(p, re.compile(p["regex"], re.I | re.M))
                for p in sorted(PATTERNS, key=lambda p: -p["weight"]) if p["weight"] >= min_weight]
    hits = []
    pattern_counter = Counter()
    for pi, si, s in sentences:
        plain = s.replace(DOT, ".")
        spans = []
        has_citation = bool(CITATION_RE.search(unmask(s, store)))
        for p, rx in compiled:
            for m in rx.finditer(plain):
                a, b = m.span()
                if any((x <= a and b <= y) or (c == p["id"][0] and a < y and x < b) for x, y, c in spans):
                    continue  # Teil/Überlappung eines bereits gemeldeten Treffers
                if p["id"] == "V02" and has_citation:
                    continue  # Zuschreibung ist im selben Satz belegt
                spans.append((a, b, p["id"][0]))
                pattern_counter[p["id"]] += 1
                hits.append(dict(par=pi, sent=si, id=p["id"], label=p["label"], weight=p["weight"],
                                 match=m.group(0), note=p["note"]))
        for m in GENITIVE_CHAIN_RE.finditer(plain):
            pattern_counter["N02"] += 1
            hits.append(dict(par=pi, sent=si, id="N02", label="Genitiv-/Nominalkette", weight=2,
                             match=m.group(0), note="Lässt sich die Kette mit einem Verb auflösen? Fachbegriffe als Einheit erhalten."))
        if DIES_RE.search(plain):
            pattern_counter["R08"] += 1
            hits.append(dict(par=pi, sent=si, id="R08", label="'Dies/Das' ohne Bezugsnomen", weight=1,
                             match=plain.split()[0] + " " + plain.split()[1],
                             note="Worauf bezieht sich 'Dies'? Bei mehreren möglichen Bezügen ein Nomen ergänzen ('Dieser Effekt …')."))

    # --- Statistik ---------------------------------------------------------
    lengths = [len(words(s)) for _, _, s in sentences]
    stats = {}
    if lengths:
        mean = statistics.mean(lengths)
        sd = statistics.pstdev(lengths) if len(lengths) > 1 else 0.0
        stats = dict(
            paragraphs=len(paras), sentences=len(sentences), words=sum(lengths),
            mean_len=round(mean, 1), sd_len=round(sd, 1),
            cv_len=round(sd / mean, 2) if mean else 0.0,
            long_30=sum(1 for n in lengths if n > 30),
            long_40=sum(1 for n in lengths if n > 40),
        )
        nominal = sum(len(NOMINAL_RE.findall(s)) for _, _, s in sentences)
        stats["nominalizations_per_sentence"] = round(nominal / len(sentences), 2)
        dashes = len(re.findall(r"\s[–—]\s", masked))
        stats["dashes_per_1000_words"] = round(1000 * dashes / max(1, sum(lengths)), 1)

    # Satzanfänge
    openers = Counter()
    for _, _, s in sentences:
        w = words(s)
        if w:
            openers[w[0].lower()] += 1
    rep_openers = {k: v for k, v in openers.items() if v >= 3 and v / max(1, len(sentences)) >= 0.12}

    # Konnektoren am Satzanfang
    conn = Counter()
    for _, _, s in sentences:
        low = s.lower().replace(DOT, ".")
        for c in CONNECTORS:
            if low.startswith(c + " ") or low.startswith(c + ","):
                conn[c] += 1
    conn_share = round(sum(conn.values()) / max(1, len(sentences)), 2)

    # Dreierreihen
    triplets = []
    for pi, si, s in sentences:
        for m in TRIPLET_RE.finditer(s.replace(DOT, ".")):
            if "⟦" in m.group(0) or any(ch.isdigit() for ch in m.group(0)):
                continue
            triplets.append(dict(par=pi, sent=si, match=m.group(0)))
    triplet_paras = len({t["par"] for t in triplets})

    # Redundanzkandidaten: ähnliche Sätze in verschiedenen Absätzen
    redundancy = []
    sets = [(pi, si, content_set(s)) for pi, si, s in sentences]
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            a, b = sets[i][2], sets[j][2]
            if len(a) < 4 or len(b) < 4:
                continue
            jac = len(a & b) / len(a | b)
            if jac >= 0.45:
                redundancy.append(dict(a=f"{sets[i][0]}.{sets[i][1]}", b=f"{sets[j][0]}.{sets[j][1]}",
                                       jaccard=round(jac, 2), shared=sorted(a & b)[:8]))

    # Satzliste für die Satz-für-Satz-Analyse
    sent_list = [dict(id=f"{pi}.{si}", words=len(words(s)), text=unmask(s, store)) for pi, si, s in sentences]

    findings = dict(
        stats=stats,
        pattern_counts=dict(pattern_counter.most_common()),
        hits=hits,
        repeated_openers=rep_openers,
        connectors_at_start=dict(conn.most_common()),
        connector_share=conn_share,
        triplets=triplets,
        triplet_paragraph_share=round(triplet_paras / max(1, len(paras)), 2),
        redundancy=redundancy,
        sentences=sent_list,
    )
    findings["signals"] = summarize(findings)
    return findings


def summarize(f):
    """Auffällige Häufungen als Hinweise formulieren (keine Herkunftsaussage)."""
    s = f["stats"]
    sig = []
    if not s:
        return sig
    if s["sentences"] >= 8 and s["cv_len"] < 0.30:
        sig.append(f"Gleichförmige Satzlängen (Variationskoeffizient {s['cv_len']}; typisch für variierte Prosa > 0,35).")
    if s["long_40"]:
        sig.append(f"{s['long_40']} Satz/Sätze über 40 Wörter – auf Verschachtelung prüfen.")
    if s["nominalizations_per_sentence"] > 2.5:
        sig.append(f"Hohe Nominalisierungsdichte ({s['nominalizations_per_sentence']} pro Satz) – Verbalstil prüfen.")
    if s["dashes_per_1000_words"] > 8:
        sig.append(f"Viele Gedankenstriche ({s['dashes_per_1000_words']} pro 1000 Wörter).")
    if f["connector_share"] > 0.35:
        sig.append(f"{int(f['connector_share'] * 100)} % der Sätze beginnen mit einem Konnektor – mechanische Übergänge prüfen.")
    for w, n in f["repeated_openers"].items():
        sig.append(f"Satzanfang '{w}' {n}× – Satzanfänge variieren, sofern inhaltlich sinnvoll.")
    if f["triplet_paragraph_share"] >= 0.5 and len(f["triplets"]) >= 3:
        sig.append(f"Dreierreihen in {int(f['triplet_paragraph_share'] * 100)} % der Absätze – auf Schablone prüfen.")
    heavy = [h for h in f["hits"] if h["weight"] == 3]
    if heavy:
        sig.append(f"{len(heavy)} Treffer mit Gewicht 3 (fast immer inhaltsleer) – vorrangig prüfen.")
    if f["redundancy"]:
        sig.append(f"{len(f['redundancy'])} Satzpaar(e) mit hoher inhaltlicher Überschneidung – Redundanz prüfen.")
    return sig


def report(f):
    out = []
    s = f["stats"]
    out.append("# Vorabscan (Kandidaten, keine Urteile)\n")
    if not s:
        out.append("Kein analysierbarer Fließtext gefunden.")
        return "\n".join(out)
    out.append(f"Absätze: {s['paragraphs']} | Sätze: {s['sentences']} | Wörter: {s['words']}")
    out.append(f"Satzlänge: Mittel {s['mean_len']} | SD {s['sd_len']} | VK {s['cv_len']} | >30 W.: {s['long_30']} | >40 W.: {s['long_40']}")
    out.append(f"Nominalisierungen/Satz: {s['nominalizations_per_sentence']} | Gedankenstriche/1000 W.: {s['dashes_per_1000_words']}")
    out.append(f"Konnektor am Satzanfang: {int(f['connector_share'] * 100)} % {f['connectors_at_start'] or ''}")
    out.append("")
    out.append("## Auffällige Häufungen")
    out.extend([f"- {x}" for x in f["signals"]] or ["- keine"])
    out.append("")
    out.append("## Mustertreffer (nach Satz)")
    if not f["hits"]:
        out.append("- keine")
    for h in sorted(f["hits"], key=lambda h: (h["par"], h["sent"], -h["weight"])):
        out.append(f"- [{h['par']}.{h['sent']}] {h['id']} (G{h['weight']}) {h['label']}: »{h['match']}«\n    Prüffrage: {h['note']}")
    if f["triplets"]:
        out.append("\n## Dreierreihen")
        out.extend(f"- [{t['par']}.{t['sent']}] »{t['match']}«" for t in f["triplets"])
    if f["redundancy"]:
        out.append("\n## Redundanzkandidaten")
        out.extend(f"- {r['a']} ↔ {r['b']} (Jaccard {r['jaccard']}): {', '.join(r['shared'])}" for r in f["redundancy"])
    out.append("\n## Sätze")
    out.extend(f"[{x['id']}] ({x['words']} W.) {x['text']}" for x in f["sentences"])
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", help="Textdatei oder '-' für stdin")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--min-weight", type=int, default=1, choices=[1, 2, 3])
    a = ap.parse_args()
    text = sys.stdin.read() if a.file == "-" else Path(a.file).read_text(encoding="utf-8")
    f = analyse(text, a.min_weight)
    print(json.dumps(f, ensure_ascii=False, indent=1) if a.json else report(f))


if __name__ == "__main__":
    main()
