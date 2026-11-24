# Bewertungskriterien

## Teil 1 – Kriterienkatalog für die Stilkontrolle (Modus K)

Jedes Kriterium erhält eine Stufe von 1 (ungenügend) bis 5 (sehr gut), eine Begründung mit Textstelle und einen konkreten Verbesserungsvorschlag. Es gibt keine Gesamtnote ohne Einzelbegründungen.

| # | Kriterium | 5 – sehr gut | 3 – ausreichend | 1 – ungenügend | Prüfhilfen |
|---|---|---|---|---|---|
| 1 | **Wissenschaftliche Präzision** | Größen, Bedingungen und Gültigkeitsbereiche sind genannt; Hedging passt zur Evidenz | einzelne vage Angaben („erheblich“, „viele Faktoren“) | Platzhalter statt Aussagen; Allaussagen ohne Bereich | V03, V04, E02, N06; `scientific_argumentation.md` §1–2 |
| 2 | **Sprachliche Natürlichkeit** | idiomatisches Wissenschaftsdeutsch, keine Floskeln | einzelne Floskeln oder Lehnübersetzungen | Häufung von Metakommentaren, Modewörtern, Schablonen | Kategorien E, F, N05, N07, R; Scan-Gewicht G3 |
| 3 | **Fachterminologische Korrektheit** | Termini korrekt und konstant; Abkürzungen eingeführt | vereinzelte Synonymvariation | Verwechslung von Größen, falsche Termini | `technical_writing.md`; F-Befunde |
| 4 | **Grammatik und Syntax** | fehlerfrei | vereinzelte Fehler ohne Sinnverlust | Fehler mit Sinnverlust (Bezug, Kongruenz) | G-Befunde; R08 |
| 5 | **Satzstruktur** | Hauptsache im Hauptsatz; Länge folgt der Funktion | einzelne Schachtelsätze oder gleichförmiger Rhythmus | durchgehend verschachtelt oder monoton | Scan: VK, >40 Wörter; `sentence_structures.md` |
| 6 | **Informationsdichte** | jeder Satz trägt Information | einige leere Sätze/Satzteile | viele Sätze ohne Information | F01–F03, S04, N08; Nominalisierungen/Satz |
| 7 | **Redundanzfreiheit** | keine unnötige Wiederholung | gelegentliche Absatzresümees | wiederholte Aussagen zwischen Absätzen | S06, A03; Scan-Redundanzkandidaten |
| 8 | **Argumentative Kohärenz** | Relationen korrekt benannt; Behauptung–Begründung–Beleg vollständig | Lücken oder unpassende Konnektoren | Scheinkausalität, Sprünge, unbelegte Kernaussagen | L/B-Befunde; `transitions_and_connectors.md` |
| 9 | **Stilistische Konsistenz** | einheitliche Konventionen (Passiv/wir, Gl./Gleichung, Dezimalzeichen) | gelegentliche Wechsel | Stilbrüche (werblich ↔ technisch) | `german_academic_standards.md` §4–5 |

**Beispiel (T3, Original):** Präzision 2 (Wertungen statt Werte; „nahezu vollständig“ unbelegt) · Natürlichkeit 1 (5 G3-Floskeln in 12 Sätzen) · Terminologie 3 („Materialbearbeitung“ statt „Ablation“) · Grammatik 5 · Satzstruktur 3 (VK 0,26: gleichförmig) · Informationsdichte 2 (Sätze 2.4, 4.1, 4.2 ohne Information) · Redundanz 3 (Absatz 4 wiederholt Absatz 1) · Kohärenz 1 (falsche physikalische Begründung, unbelegte Zuschreibung) · Konsistenz 3 (Wechsel zwischen werbendem und technischem Register).

## Teil 2 – Abnahmekriterien für die Skill (Qualitätsprüfung)

| # | Prüfpunkt (aus dem Auftrag) | Messung | Bestanden, wenn |
|---|---|---|---|
| P1 | Erkennt künstlich wirkende Formulierungen | Scan + manuelle Analyse T3 | alle 12 erwarteten Mustertypen erkannt; ≥ 5 G3-Treffer |
| P2 | Erkennt legitime Standardformulierungen | T4, T5, T6: „Bewusst belassen“-Liste; Scan-Gewichte | keine G2/G3-Treffer in T4; „Hierbei bezeichnen“, „Es sei“, belegtes „etabliert“, einzelnes „Darüber hinaus“ bleiben |
| P3 | Vermeidet unnötige Synonymersetzungen | Änderungsprotokolle | keine Änderung, deren Grund nur „Variation“ ist |
| P4 | Verbessert Satzbau und Lesbarkeit | Vorher/Nachher: G2/G3-Treffer, Wörter, Nominalisierungen/Satz, VK | Treffer G≥2 → 0; Wortzahl sinkt bei Floskeltexten; keine Verschlechterung bei guten Texten |
| P5 | Fachliche Aussage bleibt erhalten | Satzweiser Abgleich (Modalität, Bereich, Richtung) | keine Statusverschiebung; F/B nur markiert |
| P6 | Gleichungen und Quellen unverändert | `check_integrity.py` + Negativtests | alle Revisionen OK; alle 11 Verfälschungen erkannt; keine Fehlalarme |
| P7 | Kein künstlich vereinheitlichter Stil | Vergleich der Revisionen | Passiv/wir-Konvention und Satzrhythmus des Originals erhalten; keine Einheitsform für Absätze |
| P8 | Guter Text bleibt unverändert | T4 | Revision identisch mit Original |
