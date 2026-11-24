# -*- coding: utf-8 -*-
"""Bewertet die Blindtest-Läufe objektiv (Integrität, Floskelreduktion, Markierungen)."""
import difflib
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
WS = Path(__file__).resolve().parent
SKILL = WS.parent / "scientific-german-writing"
sys.path.insert(0, str(SKILL / "scripts"))
import scan_text  # noqa: E402
import check_integrity as ci  # noqa: E402

CIT = re.compile(r"\[\d+(?:[,–\-]\s*\d+)*\]|\([A-ZÄÖÜ][^()]*?(?:19|20)\d\d[^()]*\)|[A-ZÄÖÜ]\w+ et al\. \((?:19|20)\d\d\)")
AI_CLAIM = re.compile(r"(KI|ChatGPT|Sprachmodell|maschinell)[^.\n]{0,40}(generiert|verfasst|geschrieben|erstellt)|stammt (vermutlich|wahrscheinlich) (von|aus) (einer )?KI", re.I)


def strip_ann(t):
    return re.sub(r"\s*⟨[^⟩]*⟩", "", t)


def g2(text):
    f = scan_text.analyse(text)
    return sum(h["weight"] >= 2 for h in f["hits"]), sum(h["weight"] == 3 for h in f["hits"]), f["stats"].get("words", 0)


def assertions(case, orig, rev, report):
    a = []
    revp = strip_ann(rev)
    anns = re.findall(r"⟨([^⟩]*)⟩", rev) + re.findall(r"⟨([^⟩]*)⟩", report)
    ann_txt = " ".join(anns).lower()
    rep = report.lower()
    def add(t, ok, ev=""):
        a.append({"text": t, "passed": bool(ok), "evidence": ev})
    d = ci.compare(ci.inventory(orig), ci.inventory(rev))
    add("Integrität: alle geschützten Elemente unverändert", not d, json.dumps(d, ensure_ascii=False)[:300])
    new_cits = set(CIT.findall(revp)) - set(CIT.findall(orig))
    add("Keine neuen Literaturverweise erfunden", not new_cits, str(new_cits))
    add("Kein Herkunftsurteil ('KI-generiert') im Bericht", not AI_CLAIM.search(report), (AI_CLAIM.search(report) or [""])[0] if AI_CLAIM.search(report) else "")
    o2, o3, ow = g2(orig)
    r2, r3, rw = g2(revp)
    if case == "t4":
        ratio = difflib.SequenceMatcher(None, orig.strip(), revp.strip()).ratio()
        add("Guter Text weitgehend unverändert (Ähnlichkeit >= 0,97)", ratio >= 0.97, f"ratio={ratio:.3f}")
    else:
        add("Treffer mit Gewicht >= 2 reduziert", r2 < o2, f"{o2} -> {r2}")
        # V02 ('Studien zeigen') darf wörtlich bleiben, wenn es als B markiert ist (SKILL.md, Schritt 5)
        rhits = scan_text.analyse(revp)["hits"]
        marked_b = "quelle" in ann_txt or "beleg" in ann_txt or "[quelle]" in revp.lower() or "[beleg" in revp.lower()
        r3_eff = sum(h["weight"] == 3 and not (h["id"] == "V02" and marked_b) for h in rhits)
        add("Keine unmarkierten G3-Floskeln mehr", r3_eff == 0, f"{o3} -> {r3_eff} (roh {r3})")
    if case == "t1":
        add("F-Markierung zur Dotierungs-Aussage", "dotierung" in ann_txt or ("f:" in ann_txt and "v_a" in ann_txt) or ("dotierung" in rep and "f" in rep and "prüf" in rep), "")
        add("Hedging 'typischerweise' und 'in guter Näherung' erhalten", "typischerweise" in revp and "in guter Näherung" in revp)
    if case == "t3":
        add("Physikfehler Photonenenergie/Wellenlänge erkannt", ("photonenenergie" in ann_txt) or ("hc/" in ann_txt) or ("hc/" in rep) or ("photonenenergie" in rep and ("sinkt" in rep or "falsch" in rep)), "")
        add("Falsche Aussage nicht eigenmächtig umgeschrieben (Original-Satz oder Markierung erhalten)",
            ("Photonenenergie mit zunehmender Wellenlänge steigt" in revp) or ("photonenenergie" in ann_txt), "")
        add("B-Markierung für 'Studien zeigen' ohne Quelle", "quelle" in ann_txt or "beleg" in ann_txt or "[quelle]" in revp.lower() or "[beleg" in revp.lower(), "")
        add("Keine neuen Fachaussagen eingefügt (Wortzahl der Revision <= Original)", rw <= ow, f"{ow} -> {rw}")
    if case == "t6":
        add("B-Markierung für 'Studien zeigen' ohne Quelle", "quelle" in ann_txt or "beleg" in ann_txt, "")
        add("Belegter Satz 'zunehmend … etabliert (Weber et al., 2019; …)' erhalten", "etabliert (Weber et al., 2019; Klein und Hoffmann, 2021)" in revp)
    if case == "t7":
        add("'wir'-Konvention der Informatik erhalten", re.search(r"\bWir\b", revp) is not None)
        add("'bekanntlich'-Behauptung belegt/markiert oder entfernt+protokolliert", ("bekanntlich" not in revp and "bekanntlich" in rep) or "beleg" in ann_txt or "quelle" in ann_txt)
        add("'signifikant' (nicht statistisch) behandelt", "signifikant" not in revp or "signifikant" in ann_txt)
    return a, dict(g2_before=o2, g2_after=r2, words_before=ow, words_after=rw)


def main():
    rows = []
    for case in ["t1", "t3", "t4", "t6", "t7"]:
        orig = (WS / "inputs" / f"{case}.md").read_text(encoding="utf-8")
        for cfg in ["with_skill", "without_skill"]:
            out = WS / "iteration-1" / case / cfg / "outputs"
            if not (out / "revised.md").exists():
                continue
            rev = (out / "revised.md").read_text(encoding="utf-8")
            rep = (out / "report.md").read_text(encoding="utf-8") if (out / "report.md").exists() else ""
            a, m = assertions(case, orig, rev, rep)
            (out.parent / "grading.json").write_text(json.dumps({"expectations": a, "metrics": m}, ensure_ascii=False, indent=1), encoding="utf-8")
            rows.append((case, cfg, sum(x["passed"] for x in a), len(a), m, [x for x in a if not x["passed"]]))
    for case, cfg, p, n, m, fails in rows:
        print(f"{case} {cfg:14s} {p}/{n}  G>=2 {m['g2_before']}->{m['g2_after']}  Wörter {m['words_before']}->{m['words_after']}")
        for f in fails:
            print(f"    FAIL {f['text']}  {f['evidence']}")


if __name__ == "__main__":
    main()
