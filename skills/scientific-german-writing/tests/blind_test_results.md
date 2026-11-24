# Blindtest (unabhängige Instanzen)

Stand: 24.11.2026 · Ergebnisse und Einzelbewertungen: `tests/blind_test/<text>_<konfiguration>/` (revised.md, report.md, grading.json). Das Bewertungsskript `grade_blind.py` erwartet die Ordnerstruktur des Test-Arbeitsbereichs (`inputs/`, `iteration-1/`). Es liegt hier nur zur Dokumentation.

## Aufbau
- **Fünf Läufe mit Skill** (T1, T3, T4, T6, T7) und **zwei Läufe ohne Skill** (T3, T4) mit identischen Nutzeranfragen. Alle sind unabhängige Instanzen ohne Kenntnis dieses Entwicklungsverlaufs.
- Die Läufe mit Skill erhielten eine **Kopie ohne `examples/` und `tests/`**, damit sie die Musterlösungen nicht sehen konnten. Die Eingabetexte waren von Testkommentaren befreit.
- **T7 (Informatik)** wurde nur für den Blindtest geschrieben. Eine Referenzüberarbeitung gab es dafür nicht.
- Nutzeranfragen: T1 „Bitte überarbeite … Formeln nicht anfassen“; T3 „Das klingt total nach ChatGPT, mach das bitte wissenschaftlicher“; T4 „Kannst du diesen Abschnitt sprachlich verbessern?“; T6 „… die Quellen müssen genau so bleiben“; T7 „Bitte überarbeite …“.
- Bewertung: skriptbasiert (Integrität, erfundene Zitate, Herkunftsurteil, Floskelreduktion, Ähnlichkeit, textspezifische Markierungen) plus Durchsicht der Berichte.

## Ergebnis

| Lauf | Bestanden | Treffer G≥2 | Wörter | Kernbefund |
|---|---|---|---|---|
| T1 mit Skill | **7/7** | 5 → 0 | 206 → 186 | 5 sprachliche Änderungen, 3 F-Markierungen (Dotierung; **Bezugsorte beim Smith-Kriterium**, die der eigene Test übersehen hatte; L vs. $L_{\mathrm{eff}}$); Notationshinweis $g_B^{\max}$/$g_B$ |
| T3 mit Skill | **9/9** | 16 → 2¹ | 199 → 132 | Physikfehler markiert, nicht umgeschrieben; „Ob ein Text nach ChatGPT klingt, beurteile ich nicht“; Kategorienfehler („Forschungsfeld erhöht Präzision“) korrigiert |
| T3 **ohne** Skill | 6/9 | 16 → 0 | 199 → **215** | Physikfehler erkannt, aber **selbst umgeschrieben**; **neue Fachinhalte** eingefügt (thermische Relaxationszeit, Hydroxylapatit, Fluenz); Aussage „nahezu vollständig vermieden“ **abgeschwächt**; Zahl verändert (doppelte 2,94 µm); konkrete Literatur vorgeschlagen |
| T4 mit Skill | **4/4** | 0 → 0 | 140 → 140 | Fließtext **wortgleich**; eine F-Markierung (Kernradius ↔ Intensität gilt nach Gl. 3.2 nicht für kleine $V$); begründete „Bewusst belassen“-Liste |
| T4 **ohne** Skill | 3/4 | 0 → 0 | 140 → 150 | fast jeder Satz umformuliert (Ähnlichkeit 0,85); Synonymtausch („deshalb“ → „daher“, „dafür“ → „hierfür“); Fachaussage eigenmächtig geändert |
| T6 mit Skill | **7/7** | 2 → 1² | 196 → 186 | 2 Änderungen, 2 B-Markierungen, alle 7 Zitate unverändert, Mischung der Zitierstile nur angemerkt |
| T7 mit Skill | **8/8** | 6 → 0 | 147 → 115 | „wir“-Konvention erhalten; „signifikant“ (nicht statistisch) → „deutlich“; „bekanntlich“ → B/F; fehlende Definition von $p_t$, $\alpha_t$ markiert |

¹ Verbleibend: „unverzichtbar“ (als B markiert und bewusst belassen, weil Abschwächen eine Inhaltsänderung wäre) und der Ausblick mit Strukturhinweis. Beides ist regelkonform.
² „Studien zeigen“ wörtlich belassen und als B markiert, zulässig nach SKILL.md Schritt 5.

**Summe: mit Skill 35/35, ohne Skill 9/13.** Der Unterschied liegt genau in den Integritätsregeln. Ohne Skill wird gut geschrieben, aber eigenmächtig fachlich umgearbeitet und Inhalt hinzugefügt. Mit Skill werden nur sprachliche Mängel behoben, und alles Fachliche wird dem Autor zur Entscheidung vorgelegt.

## Erkenntnisse und daraus folgende Änderungen an der Skill

| # | Beobachtung | Änderung |
|---|---|---|
| 1 | Beide Läufe mit Skill fanden fachliche Unschärfen in Texten, die sprachlich gut sind (T4 Kernradius, T1 Smith-Kriterium). Der eigene Selbsttest hatte T4 als „keine Änderung, kein Befund“ bewertet, und das war unvollständig. | SKILL.md Schritt 5: neuer Absatz **„Fachliche Gegenprüfung auch bei guten Texten“**. Referenzergebnisse T1/T4 um die Befunde ergänzt; Test „T4: F-Markierung vorhanden“ hinzugefügt. |
| 2 | Uneinheitliche Markierungen (`[Beleg?]` im T3-Lauf), weil SKILL.md selbst `[Beleg?]` nannte | SKILL.md: einheitlich `⟨B: …⟩`, mit Begründung (Skripte erkennen nur ⟨…⟩); Regressionstest gegen eckige Platzhalter |
| 3 | T7-Lauf strich einen unbelegten Wertungssatz komplett (offengelegt). Das ist vertretbar, aber Grenzfall der Integritätsregel. | SKILL.md Schritt 6: Regel **„Unbelegte Wertungssätze nicht stillschweigend löschen“**: bevorzugt markieren, Streichung nur mit Protokolleintrag |
| 4 | Alle Läufe mit Skill hielten die Ausgabevorlagen ein (Protokoll, „Unverändert gelassen“, Integritätsprüfung) und nutzten beide Skripte | keine Änderung nötig |
| 5 | Kein Lauf mit Skill fällte ein Herkunftsurteil, auch nicht bei der Anfrage „klingt nach ChatGPT“ | keine Änderung nötig |

Nach den Änderungen: `python tests/run_tests.py` → **46/46 bestanden**.

## Grenzen des Blindtests
- Die unabhängigen Instanzen sind dasselbe Modell wie der Entwickler, es gab keine menschliche Fachlektorin. Die Ähnlichkeit im Urteil kann deshalb überschätzt sein.
- Pro Text gab es je einen Lauf, daher keine Aussage zur Streuung zwischen Läufen.
- Die Bewertung ist teils skriptbasiert (Stichwortsuche in Anmerkungen). Die Berichte wurden zusätzlich von Hand durchgesehen.
- Die Läufe ohne Skill wurden nur für T3 und T4 durchgeführt.
