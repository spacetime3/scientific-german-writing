# -*- coding: utf-8 -*-
"""Automatisierte Regressionstests für scan_text.py und check_integrity.py.

Aufruf (aus dem Skill-Verzeichnis):  python tests/run_tests.py
Die qualitativen Tests (Überarbeitungsqualität) sind in tests/test_results.md dokumentiert.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
for s in (sys.stdout,):
    try:
        s.reconfigure(encoding="utf-8")
    except Exception:
        pass

import scan_text  # noqa: E402
import check_integrity as ci  # noqa: E402

T = ROOT / "tests" / "texts"
R = ROOT / "tests" / "results"
FILES = {
    "t1": "t1_physik_theorie.md", "t2": "t2_ingenieur.md", "t3": "t3_ki_floskeln.md",
    "t4": "t4_gut_formuliert.md", "t5": "t5_gleichungen.md", "t6": "t6_fachbegriffe_quellen.md",
}
results = []


def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))


def scan(path_or_text, is_text=False):
    text = path_or_text if is_text else Path(path_or_text).read_text(encoding="utf-8")
    return scan_text.analyse(text)


def ids(f, sent=None):
    return {h["id"] for h in f["hits"] if sent is None or f"{h['par']}.{h['sent']}" == sent}


# --- 1. Erkennung künstlich wirkender Formulierungen (Prüfpunkt 1) ------------
f3 = scan(T / FILES["t3"])
expected_t3 = {"E01", "E02", "E03", "F01", "F02", "F03", "V02", "S01", "S04", "S05", "N05", "U02"}
check("T3: alle erwarteten Floskelmuster erkannt", expected_t3 <= ids(f3), f"fehlend: {expected_t3 - ids(f3)}")
check("T3: >= 5 Treffer mit Gewicht 3", sum(h["weight"] == 3 for h in f3["hits"]) >= 5)
check("T3: Signal gleichförmige Satzlänge", any("Gleichförmige" in s for s in f3["signals"]))
check("T3: Signal Dreierreihen", any("Dreierreihen" in s for s in f3["signals"]))

# --- 2. Legitime Standardformulierungen nicht als schwer gewichtet (Prüfpunkt 2, 8) --
f4 = scan(T / FILES["t4"])
check("T4 (guter Text): keine Treffer mit Gewicht >= 2", not [h for h in f4["hits"] if h["weight"] >= 2],
      str([(h["id"], h["match"]) for h in f4["hits"] if h["weight"] >= 2]))
check("T4: keine Häufungssignale", not f4["signals"], str(f4["signals"]))
f5 = scan(T / FILES["t5"])
check("T5: 'Hierbei bezeichnen' nur G1 (Variablenerklärung)", all(h["weight"] == 1 for h in f5["hits"] if h["id"] == "U04"))
check("T5: keine G3-Treffer in Herleitung", not [h for h in f5["hits"] if h["weight"] == 3])
math = scan("Es sei $f$ stetig auf $[a,b]$. Dann gilt der Mittelwertsatz.", is_text=True)
check("Mathematik: 'Es sei' höchstens G1", all(h["weight"] == 1 for h in math["hits"]))

# --- 3. Belegprüfung: V02 nur ohne Literaturverweis im Satz -----------------
f6 = scan(T / FILES["t6"])
check("T6: 'Studien zeigen' ohne Quelle -> V02", "V02" in ids(f6, "2.3"))
cited = scan("Studien zeigen, dass HIP die Porosität reduziert [7].", is_text=True)
check("V02 entfällt bei Quelle im Satz", "V02" not in ids(cited))

# --- 4. Fachlich fragwürdige Allaussage als Kandidat (Phase IV) --------------
f1 = scan(T / FILES["t1"])
check("T1: 'stets unabhängig' als V04-Kandidat", "V04" in ids(f1, "2.3"))
check("T1: Blähnomen+Blähverb erkannt (N08)", "N08" in ids(f1, "4.1"))
check("Kein Fehlalarm: zweistufiger Genitiv ('der Dotierung des Faserkerns')", "N02" not in ids(f1, "2.3"))
chain = scan("Die Prüfung der Sicherheit des Produkts erfolgt durch den Techniker.", is_text=True)
check("Dreistufige Genitivkette erkannt (Mainz-Beispiel)", "N02" in ids(chain))

# --- 5. Satzsegmentierung robust gegen Abkürzungen und Formeln --------------
f6_first = [s["text"] for s in f6["sentences"]][0]
check("Abkürzung 'engl.' trennt keinen Satz", "Laser Powder Bed Fusion" in f6_first, f6_first[:60])
seg = scan("Nach Gl. (2.8) gilt $x = 1.5$. Abb. 3 zeigt z. B. den Verlauf.", is_text=True)
check("Gl./Abb./z. B./Dezimalpunkt korrekt segmentiert", len(seg["sentences"]) == 2, str([s["text"] for s in seg["sentences"]]))

# --- 6. Überarbeitung reduziert Floskeln (Prüfpunkt 4) -----------------------
f3r = scan(R / "t3_revised.md")
check("T3 überarbeitet: keine G3-Treffer mehr", not [h for h in f3r["hits"] if h["weight"] == 3],
      str([(h["id"], h["match"]) for h in f3r["hits"] if h["weight"] == 3]))
check("T3 überarbeitet: Satzlängen variabler", f3r["stats"]["cv_len"] > f3["stats"]["cv_len"],
      f"{f3['stats']['cv_len']} -> {f3r['stats']['cv_len']}")

# --- 7. Integrität: alle dokumentierten Revisionen bestehen (Prüfpunkt 5, 6) --
for k, fn in FILES.items():
    o = ci.inventory((T / fn).read_text(encoding="utf-8"))
    r = ci.inventory((R / f"{k}_revised.md").read_text(encoding="utf-8"))
    d = ci.compare(o, r)
    check(f"Integrität {k}: Revision vollständig", not d, str(d))

# T4: guter Text bleibt sprachlich unverändert (Prüfpunkt 8); fachliche Markierung ist erlaubt
import re  # noqa: E402
_strip = lambda t: re.sub(r"\s*⟨[^⟩]*⟩", "", re.sub(r"<!--.*?-->\s*", "", t, flags=re.S)).strip()
t4o = (T / FILES["t4"]).read_text(encoding="utf-8")
t4r = (R / "t4_revised.md").read_text(encoding="utf-8")
check("T4: Fließtext identisch mit Original (ohne Anmerkungen)", _strip(t4o) == _strip(t4r))
check("T4: F-Markierung zum Kernradius-Satz (Blindtest-Befund)", "⟨F:" in t4r and "Kernradius" in t4r)

# Markierungsformat: nur ⟨…⟩, keine eckigen Platzhalter
for k in FILES:
    txt = (R / f"{k}_revised.md").read_text(encoding="utf-8")
    check(f"{k}: keine [Beleg?]/[Quelle]-Platzhalter", not re.search(r"\[(?:Beleg\??|Quelle)\]", txt))

# --- 8. Integritätsprüfer erkennt Verfälschungen (Negativtests) --------------
orig1 = (T / FILES["t1"]).read_text(encoding="utf-8")
orig6 = (T / FILES["t6"]).read_text(encoding="utf-8")
orig5 = (T / FILES["t5"]).read_text(encoding="utf-8")
corruptions = {
    "Zahlenwert geändert (1550 nm -> 1310 nm)": (orig1, orig1.replace("1550 nm", "1310 nm"), "quantity"),
    "Einheit geändert (MHz -> GHz)": (orig1, orig1.replace("30 MHz", "30 GHz"), "quantity"),
    "Literaturverweis entfernt ([13])": (orig1, orig1.replace(" [13]", ""), "citation"),
    "Gleichungsverweis geändert (2.8 -> 2.9)": (orig1, orig1.replace("Gleichung (2.8)", "Gleichung (2.9)"), "crossref"),
    "Index in Formel geändert (L_eff -> L)": (orig1, orig1.replace("g_B L_{\\mathrm{eff}}", "g_B L"), "math"),
    "Faktor in Formel geändert (21 -> 16)": (orig1, orig1.replace("\\approx 21", "\\approx 16"), "math"),
    "Vorzeichen in align geändert": (orig5, orig5.replace("&= -\\frac{\\alpha}{2} A_p", "&= +\\frac{\\alpha}{2} A_p"), "math"),
    "Werkstoffbezeichner geändert (Ti-6Al-4V -> Ti-6Al-7Nb)": (orig6, orig6.replace("Implantate aus Ti-6Al-4V", "Implantate aus Ti-6Al-7Nb"), "designation"),
    "Jahr im Zitat geändert (2019 -> 2018)": (orig6, orig6.replace("Weber et al., 2019; Klein", "Weber et al., 2018; Klein"), "citation"),
    "Prozentwert geändert (30 % -> 35 %)": (orig6, orig6.replace("etwa 30 %", "etwa 35 %"), "quantity"),
    "Symbol im Fließtext geändert (α' -> β')": (orig6, orig6.replace("martensitisches α'", "martensitisches β'"), "symbol"),
}
for name, (a, b, key) in corruptions.items():
    d = ci.compare(ci.inventory(a), ci.inventory(b))
    check(f"Negativtest erkannt: {name}", key in d, str(list(d)))

# Zulässige Umformulierung darf keinen Fehlalarm auslösen
ok_variant = orig1.replace("Gleichung (2.8) verdeutlicht", "Gl. (2.8) zeigt")
check("Kein Fehlalarm: 'Gleichung' -> 'Gl.'", not ci.compare(ci.inventory(orig1), ci.inventory(ok_variant)))
ann = orig1 + "\n⟨F: Gilt das auch für $v_A$ bei 1310 nm? [99]⟩"
check("Kein Fehlalarm: Prüfanmerkungen ⟨…⟩ werden ignoriert", not ci.compare(ci.inventory(orig1), ci.inventory(ann)))

# --- Ausgabe -----------------------------------------------------------------
passed = sum(ok for _, ok, _ in results)
for name, ok, detail in results:
    print(("PASS " if ok else "FAIL ") + name + ("" if ok or not detail else f"\n     -> {detail}"))
print(f"\n{passed}/{len(results)} Tests bestanden.")
sys.exit(0 if passed == len(results) else 1)
