# -*- coding: utf-8 -*-
"""Integritätsprüfung: Original vs. Überarbeitung.

Prüft, ob alle fachlich geschützten Elemente nach der sprachlichen
Überarbeitung unverändert (als Multimenge) vorhanden sind:

  math      Formeln ($…$, $$…$$, \\[…\\], equation/align-Umgebungen)
  latex     \\cite, \\ref, \\eqref, \\label
  citation  [12], [3–5], (Müller, 2020), Müller et al. (2020), Müller und Schmidt (2019)
  crossref  Gl. (3), Gleichung (3), Abb. 2, Tab. 1, Kap. 4, Abschnitt 2.3 …
  quantity  Zahl + Einheit (1550 nm, 10 mW, 3,2 dB, 25 %)
  number    alle übrigen Zahlen
  symbol    griechische Buchstaben und indizierte Größen außerhalb von Formeln (λ, Δn, n_eff, g_B)
  acronym   Abkürzungen aus Großbuchstaben (SBS, SMF-28, FWHM)
  term      Begriffe aus --terms (eine Zeile je Fachbegriff)

Verweistypen werden normalisiert (Gl. = Gleichung, Abb. = Abbildung),
damit 'Gl. (3)' -> 'Gleichung (3)' nicht als Fehler zählt.

Aufruf:
  python check_integrity.py original.md revision.md [--terms terms.txt]
  python check_integrity.py original.md --inventory      # Schutzinventar
Exit-Code 0 = alles erhalten, 1 = Abweichungen (manuell prüfen).
"""
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8")
    except Exception:
        pass

MATH_RE = re.compile(
    r"\$\$.+?\$\$|\$[^$\n]+?\$|\\\[.+?\\\]|\\\(.+?\\\)|"
    r"\\begin\{(equation|align|eqnarray|gather|multline)\*?\}.+?\\end\{\1\*?\}",
    re.S,
)
LATEX_RE = re.compile(r"\\(?:cite[pt]?|eqref|ref|autoref|cref|label)\{[^}]*\}")
CIT_NUM_RE = re.compile(r"\[\s*\d+(?:\s*[,–\-]\s*\d+)*\s*\]")
CIT_PAREN_RE = re.compile(
    r"\((?:[^()]*?[A-ZÄÖÜ][\wäöüß\-]+[^()]*?\b(?:1[89]|20)\d\d[a-z]?(?:,\s*S\.\s*\d+(?:[–\-]\d+)?)?[^()]*?)\)"
)
CIT_NARR_RE = re.compile(
    r"\b[A-ZÄÖÜ][\wäöüß\-]+(?:\s+(?:et al\.|und|&)\s*(?:[A-ZÄÖÜ][\wäöüß\-]+)?)?\s+\((?:1[89]|20)\d\d[a-z]?(?:,\s*S\.\s*\d+)?\)"
)
CROSSREF_RE = re.compile(
    r"\b(Gl\.|Gln\.|Gleichungen|Gleichung|Abb\.|Abbildungen|Abbildung|Tab\.|Tabellen|Tabelle|"
    r"Kap\.|Kapitel|Abschn\.|Abschnitt|Anhang|Fig\.|Eq\.|Formel)\s*~?\s*"
    r"(\(?\s*[A-Z]?\d+(?:\.\d+)*[a-z]?\s*\)?(?:\s*(?:–|-|bis|und|,)\s*\(?\s*[A-Z]?\d+(?:\.\d+)*[a-z]?\s*\)?)*)"
)
REF_TYPES = {
    "gl.": "Gl", "gln.": "Gl", "gleichung": "Gl", "gleichungen": "Gl", "eq.": "Gl", "formel": "Gl",
    "abb.": "Abb", "abbildung": "Abb", "abbildungen": "Abb", "fig.": "Abb",
    "tab.": "Tab", "tabelle": "Tab", "tabellen": "Tab",
    "kap.": "Kap", "kapitel": "Kap", "abschn.": "Abschn", "abschnitt": "Abschn", "anhang": "Anhang",
}
UNITS = (
    r"(?:[kMGTmµμnpf]?(?:m|s|Hz|W|J|eV|V|A|Ω|Pa|N|T|g|L|l|F|H|S|C|K|rad|sr|mol|cd|lm|lx|Gy|Sv|Bq)"
    r"|°C|°|%|‰|dB(?:m|i)?|bar|mbar|min|h|ppm|ppb|Nm|kWh|Wh|1/s|s⁻¹|m⁻¹|cm⁻¹)"
    r"(?:\s*/\s*[kMGmµμnp]?(?:m|s|Hz|W|J|V|A|K|g|L|l|mol|km|min|h)(?:²|³|\^?\d)?)?(?:²|³|⁻¹|\^-?\d)?"
)
NUM = r"[−\-+]?\d+(?:[.,]\d+)?(?:\s*(?:·|×|x|\\cdot|\\times)\s*10\^?\{?[−\-]?\d+\}?)?|10\^\{?[−\-]?\d+\}?"
QUANTITY_RE = re.compile(r"(?<![\w.,^\-])(" + NUM + r")\s*(" + UNITS + r")(?![\wäöüÄÖÜß])")
NUMBER_RE = re.compile(r"(?<![\w.,^\-])(?:" + NUM + r")(?![\w])|(?<=\s)[−\-]\d+(?:[.,]\d+)?(?![\w])")
SYMBOL_RE = re.compile(r"(?<![\w])(?:[Δδ∂∇]?[α-ωΑ-Ω](?:_\{?\w+\}?)?|[A-Za-z]{1,3}_\{?[\wäöü,]+\}?)(?![\w])")
# Werkstoff-/Laser-/Produktbezeichner: Ti-6Al-4V, Er:YAG, Nd:YVO4, SMF-28, AlSi10Mg
DESIGNATION_RE = re.compile(
    r"\b[A-Z][a-z]?-?\d+(?:[A-Z][a-z]?\d*)+(?:-\d+[A-Z][a-z]?)*\b|\b[A-Z][a-z]?(?:-\d+[A-Z][a-z]?){1,}\b|"
    r"\b[A-Z][a-z]?:[A-Z][A-Za-z0-9]{1,}\b|\b[A-Z]{2,}-\d+\b|\b[A-Z][a-z]?[A-Z][a-z]?\d+[A-Z][a-z]+\b"
)
ACRONYM_RE = re.compile(r"\b(?:[A-Z]-)?[A-ZÄÖÜ]{2,}s?\b")
ACRONYM_IGNORE = {"II", "III", "IV", "VI", "VII", "VIII", "IX", "XI", "XII"}


def norm_ws(s):
    return re.sub(r"\s+", "", s)


def norm_num(s):
    s = s.replace("−", "-").replace(",", ".").replace(" ", "").replace("\u202f", "").replace("\u2009", "")
    return s


def inventory(text, terms=()):
    inv = {k: Counter() for k in ("math", "latex", "citation", "crossref", "designation", "quantity", "number", "symbol", "acronym", "term")}
    rest = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    # Prüfanmerkungen der Skill (⟨F: …⟩, ⟨B: …⟩, ⟨L: …⟩, ⟨Autor: …⟩) sind Kommentare, kein Text
    rest = re.sub(r"⟨[^⟩]*⟩", " ", rest)

    def take(rx, key, normalize=lambda x: x):
        nonlocal rest
        for m in rx.finditer(rest):
            inv[key][normalize(m.group(0))] += 1
        rest = rx.sub(" ⟦⟧ ", rest)

    take(MATH_RE, "math", norm_ws)
    take(LATEX_RE, "latex", norm_ws)
    take(CIT_NUM_RE, "citation", norm_ws)
    take(CIT_NARR_RE, "citation", lambda x: norm_ws(x))
    take(CIT_PAREN_RE, "citation", lambda x: norm_ws(x))

    for m in CROSSREF_RE.finditer(rest):
        typ = REF_TYPES.get(m.group(1).lower(), m.group(1))
        nums = re.findall(r"[A-Z]?\d+(?:\.\d+)*[a-z]?", m.group(2))
        for n in nums:
            inv["crossref"][f"{typ} {n}"] += 1
    rest = CROSSREF_RE.sub(" ⟦⟧ ", rest)
    take(DESIGNATION_RE, "designation")

    for m in QUANTITY_RE.finditer(rest):
        inv["quantity"][f"{norm_num(m.group(1))} {m.group(2).replace('μ', 'µ')}"] += 1
    rest = QUANTITY_RE.sub(" ⟦⟧ ", rest)
    for m in NUMBER_RE.finditer(rest):
        inv["number"][norm_num(m.group(0))] += 1
    for m in SYMBOL_RE.finditer(rest):
        inv["symbol"][m.group(0)] += 1
    for m in ACRONYM_RE.finditer(rest):
        a = m.group(0)
        if a not in ACRONYM_IGNORE:
            inv["acronym"][a.rstrip("s") if a.endswith("s") and a[:-1].isupper() else a] += 1
    low = text.lower()
    for t in terms:
        if t.strip():
            inv["term"][t.strip()] = low.count(t.strip().lower())
    return inv


def compare(orig, rev):
    diff = {}
    for key in orig:
        if key == "term":
            changed = {t: (orig[key][t], rev[key].get(t, 0)) for t in orig[key] if orig[key][t] != rev[key].get(t, 0)}
            if changed:
                diff[key] = {"geändert (Original, Revision)": changed}
            continue
        missing = orig[key] - rev[key]
        added = rev[key] - orig[key]
        if missing or added:
            diff[key] = {"fehlt in Revision": dict(missing), "neu in Revision": dict(added)}
    return diff


LABELS = {
    "math": "Formeln", "latex": "LaTeX-Verweise", "citation": "Literaturverweise", "crossref": "Gleichungs-/Abbildungs-/Tabellenverweise",
    "designation": "Werkstoff-/Geräte-/Normbezeichner",
    "quantity": "Zahlenwerte mit Einheit", "number": "Weitere Zahlen", "symbol": "Symbole/Variablen im Fließtext",
    "acronym": "Abkürzungen", "term": "Fachbegriffe (--terms)",
}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("original")
    ap.add_argument("revision", nargs="?")
    ap.add_argument("--terms", help="Datei mit Fachbegriffen (einer pro Zeile)")
    ap.add_argument("--inventory", action="store_true", help="nur Schutzinventar des Originals ausgeben")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    terms = Path(a.terms).read_text(encoding="utf-8").splitlines() if a.terms else []
    o = inventory(Path(a.original).read_text(encoding="utf-8"), terms)

    if a.inventory or not a.revision:
        if a.json:
            print(json.dumps({k: dict(v) for k, v in o.items()}, ensure_ascii=False, indent=1))
        else:
            print("# Schutzinventar (darf bei der Überarbeitung nicht verändert werden)\n")
            for k, v in o.items():
                if v:
                    print(f"## {LABELS[k]} ({sum(v.values()) if k != 'term' else len(v)})")
                    print(", ".join(f"{x}" + (f" ×{n}" if n > 1 else "") for x, n in v.items()))
                    print()
        return 0

    r = inventory(Path(a.revision).read_text(encoding="utf-8"), terms)
    diff = compare(o, r)
    if a.json:
        print(json.dumps({"ok": not diff, "diff": diff}, ensure_ascii=False, indent=1))
    elif not diff:
        total = sum(sum(v.values()) for k, v in o.items() if k != "term")
        print(f"OK: Alle {total} geschützten Elemente sind in der Revision unverändert enthalten.")
    else:
        print("ABWEICHUNGEN – jede einzelne manuell prüfen:\n")
        for k, d in diff.items():
            print(f"## {LABELS[k]}")
            for kind, items in d.items():
                if items:
                    print(f"  {kind}: " + "; ".join(f"{x}" + (f" ×{n}" if isinstance(n, int) and n > 1 else (f" {n}" if not isinstance(n, int) else "")) for x, n in items.items()))
        print("\nHinweis: Eine Abweichung ist nicht automatisch ein Fehler (z. B. ausgeschriebene Zahl,"
              " zusammengelegte Verweise). Sie muss aber begründet werden können.")
    return 0 if not diff else 1


if __name__ == "__main__":
    sys.exit(main())
