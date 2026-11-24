# scientific-german-writing: Kurzanleitung

Skill für Claude zur Analyse und belegtreuen Überarbeitung deutscher wissenschaftlicher Texte (Abschlussarbeiten, Artikel, Berichte; Schwerpunkt Natur- und Ingenieurwissenschaften).

## Installation
- **Claude Code:** Ordner `scientific-german-writing/` nach `~/.claude/skills/` kopieren (für alle Projekte) oder nach `<projekt>/.claude/skills/` (nur für ein Projekt).
- **Claude.ai / Desktop:** die gepackte Datei `scientific-german-writing.skill` über „Skill speichern“ bzw. unter Einstellungen → Skills hochladen.
- Voraussetzung für die Hilfsskripte: Python ≥ 3.8, keine Zusatzpakete. Ohne Python arbeitet die Skill manuell mit denselben Regeln.

## Verwendung
Text einfügen oder Datei nennen und sagen, was gewünscht ist. Die Skill wählt den Modus selbst:

| Sie schreiben … | Modus |
|---|---|
| „Prüf mal dieses Kapitel“ / „Was ist hier sprachlich schwach?“ | A – Analyse |
| „Überarbeite den Abschnitt, Formeln nicht anfassen“ | Ü – Überarbeitung mit Änderungsprotokoll |
| „Satz für Satz bitte“ | S – Satz-für-Satz (6 Schritte je Satz) |
| „Ist der Absatz logisch aufgebaut?“ | P – Absatzanalyse |
| „Bewerte den Stil nach Kriterien“ | K – Stilkontrolle (9 Kriterien) |

Was Sie erhalten:
- sprachliche Verbesserungen nur dort, wo eine benannte Schwäche vorliegt; gute Sätze bleiben stehen;
- sichtbare Markierungen im Text: ⟨F: …⟩ fachlich fragwürdig, ⟨B: …⟩ Beleg fehlt, ⟨L: …⟩ logische Lücke, ⟨Autor: …⟩ Rückfrage. Diese Stellen müssen Sie selbst entscheiden;
- eine Integritätsprüfung: Gleichungen, Zahlen, Einheiten, Verweise und Quellen bleiben unverändert.

Was die Skill **nicht** tut: Quellen erfinden, Fachaussagen eigenmächtig „korrigieren“, beurteilen, ob ein Text von einer KI stammt, oder Texte für KI-Detektoren tarnen.

## Skripte direkt nutzen
```
python scripts/scan_text.py kapitel.md                    # Vorabscan: Muster, Satzstatistik, Redundanz
python scripts/check_integrity.py kapitel.md --inventory  # Schutzinventar
python scripts/check_integrity.py alt.md neu.md           # Vergleich nach Überarbeitung (Exit 1 bei Abweichung)
python scripts/check_integrity.py alt.md neu.md --terms begriffe.txt   # zusätzlich Fachbegriffe zählen
python tests/run_tests.py                                 # Regressionstests (46 Tests)
```
Die Eingabe kann Markdown, reiner Text oder LaTeX-Fließtext sein (`$…$`, `\begin{align}`, `\cite{}`, `\ref{}` werden erkannt).

## Aufbau
```
SKILL.md                         Arbeitsablauf, Modi, Ausgabevorlagen
references/
  ai_language_patterns.md        Musterbibliothek (55 Einträge, IDs E/U/S/F/N/R/V/A)
  standard_scientific_phrases.md Formulierungsbibliothek nach 17 Textfunktionen
  german_academic_standards.md   Konventionen der Wissenschaftssprache (belegt [Q] vs. eigene Regel [R])
  sentence_structures.md         Satzbau, Informationsstruktur, Bezüge
  transitions_and_connectors.md  Konnektoren nach logischer Relation
  scientific_argumentation.md    Epistemischer Status, Hedging, Problemklassen S/G/L/F/B
  technical_writing.md           Fachkonventionen (8 Disziplinen), Formel- und Einheitensatz
  source_references.md           Quellen mit Links und Prüfstatus
scripts/                         scan_text.py, check_integrity.py, patterns_de.py
examples/                        Vorher/Nachher, Satz- und Absatzanalyse
tests/                           7 Testtexte, Revisionen, Kriterien, Ergebnisse, run_tests.py,
                                 blind_test/ + blind_test_results.md (unabhängiger Blindtest)
```
