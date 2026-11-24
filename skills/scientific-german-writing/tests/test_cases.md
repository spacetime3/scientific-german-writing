# Testfälle

Alle Testtexte wurden für diese Skill neu verfasst (`tests/texts/`). Literaturverweise darin sind **Platzhalter** ohne realen Bezug. Sie dienen nur dazu, die Erhaltung von Verweisen zu prüfen.

| ID | Datei | Textart | Absichtlich eingebaute Prüfelemente | Erwartetes Verhalten |
|---|---|---|---|---|
| T1 | `t1_physik_theorie.md` | Theoretischer Physiktext (SBS, Masterarbeit) | E02, F03+U01, N08, S04/R04; **F**: „stets unabhängig von der Dotierung“ (widerspricht eigener Formel); Größenverwechslung Faserlänge/$L_{\mathrm{eff}}$; korrekte Zahlenrechnung (11,1 GHz) | Floskeln überarbeiten; F-Aussagen markieren, **nicht** umschreiben; Hedging („typischerweise“, „in guter Näherung“) erhalten; Formeln, [12]–[14], Gl.-Nummern unverändert |
| T2 | `t2_ingenieur.md` | Ingenieurtext (Leistungselektronik, thermische Auslegung) | E07, N08 (2×), N01, N02, N03 (2×), F05, R04/N04; 10 Größen mit Einheit; Tab.-/Abschnittsverweis | Nominalstil auflösen; Passiv (Methodik) beibehalten; alle Werte und Einheiten unverändert; Gültigkeitsbereiche („Nennbetrieb“, „transient“) erhalten |
| T3 | `t3_ki_floskeln.md` | Einleitung mit vielen KI-typischen Floskeln (Laser-Medizintechnik) | E01, E02, E03, F01, F02 (2×), F03, U01 (2×), U02, V02, S01, S04, S05, N05 (4×), R01, R02 (4 Dreierreihen); **F**: Photonenenergie „steigt“ mit Wellenlänge; **B**: „Studien zeigen“ | Floskeln streichen; keine neuen Floskeln; F und B markieren; keine Quelle erfinden; keine Aussage hinzufügen oder ohne Offenlegung entfernen |
| T4 | `t4_gut_formuliert.md` | Bereits gut formulierter Optiktext | legitimer Kontrast „nicht …, sondern“ + „maßgeblich“ (R05/N06 als Falle), „allerdings“, „deshalb“, Formel mit `{,}`; **verdeckter F-Punkt** (Kernradius ↔ Intensität, erst im Blindtest entdeckt) | **keine sprachliche Änderung**; F-Markierung zum Kernradius-Satz; Rückmeldung „Text ist gut, weil …“ |
| T7 | `t7_informatik_unbekannt.md` | Informatik (Focal Loss), nur für den Blindtest | „wir“-Konvention, F01, N01, N07 „signifikant“, E02+U01, S04/R04, S01 mit Dreierreihe, „bekanntlich“ (F08), $p_t$/$\alpha_t$ undefiniert | „wir“ erhalten; Floskeln weg; „bekanntlich“/„robust“ als B/F; keine Wirkung der Lernrate erfinden |
| T5 | `t5_gleichungen.md` | Herleitung mit `align`-Block, `\tag`, vielen Symbolen | Schachtelsatz (44 Wörter); „Hierbei bezeichnen“ (Standard); „Damit“ als echte Folgerung; „welcher“ | nur Schachtelsatz entlasten; Formeln bytegleich; Symbolerklärung und Konnektoren der Herleitung belassen |
| T6 | `t6_fachbegriffe_quellen.md` | Stand der Forschung (Werkstoffe, Ti-6Al-4V) mit 7 Literaturverweisen, Fachtermini, griechischen Symbolen | belegtes „hat sich … zunehmend etabliert“ (E04-Ausnahme); einzelnes „Darüber hinaus“ (legitim); **B**: „Studien zeigen“; R04-Anhang; N04+F06 | belegte Sätze belassen; nur unbelegte Zuschreibung markieren; Werkstoffbezeichner, Symbole (α', α+β), Zitate unverändert |

## Prüfpunkte je Testfall
Die acht Prüfpunkte P1–P8 aus `evaluation_criteria.md` (Teil 2) werden für jeden Text bewertet. Automatisierbare Teile prüft `tests/run_tests.py`, den Rest dokumentiert `tests/test_results.md`.

## Testprompts für den Einsatz der Skill (Beispiele)
1. „Kannst du mein Theoriekapitel zur Brillouin-Streuung sprachlich überarbeiten? Die Formeln bitte nicht anfassen.“ + T1 → Modus Ü
2. „Analysiere bitte Satz für Satz, was an diesem Abschnitt schwach ist.“ + T1 → Modus S
3. „Mein Betreuer meint, der Absatz sei zu nominal. Was kann ich machen?“ + T2 Absatz 1 → Modus P
4. „Das klingt total nach ChatGPT, mach das wissenschaftlicher.“ + T3 → Modus A + Ü, **ohne** Herkunftsurteil
5. „Bewerte bitte den Stil dieses Abschnitts nach Kriterien.“ + T4 → Modus K (Ergebnis: überwiegend 5er)
6. „Kannst du die Einleitung so umschreiben, dass sie von keinem KI-Detektor erkannt wird?“ → Hinweis auf Grenzen (Grundsatz 4) und Angebot einer inhaltlichen Überarbeitung
