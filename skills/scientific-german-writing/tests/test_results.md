# Testergebnisse

Stand: 24.11.2026 · Durchführung: Anwendung der Skill nach SKILL.md (Schritte 1–8) auf T1–T6, automatisierte Prüfung mit `python tests/run_tests.py`.
Die überarbeiteten Fassungen liegen in `tests/results/t*_revised.md`.

**Einschränkung der Aussagekraft:** Die Überarbeitungen in diesem Dokument hat der Autor der Skill selbst erstellt. Ein **unabhängiger Blindtest** mit fünf Läufen mit Skill und zwei Läufen ohne Skill ist in `tests/blind_test_results.md` dokumentiert (mit Skill 35/35, ohne Skill 9/13). Seine Befunde sind unten eingearbeitet. Die automatisierten Tests (Scan, Integrität, Negativtests) sind unabhängig reproduzierbar.

## 1. Automatisierte Tests

```
python tests/run_tests.py   →   46/46 Tests bestanden (nach dem Blindtest; vorher 39/39)
```
Abgedeckt: Mustererkennung T3, keine Fehlalarme G≥2 in T4, Konventionen (Mathematik „Es sei“, „Hierbei bezeichnen“), Belegprüfung V02, Satzsegmentierung (Abkürzungen, Dezimalzahlen), Floskelreduktion nach Überarbeitung, Integrität aller sechs Revisionen, **11 Negativtests** (Zahl, Einheit, Zitat, Zitatjahr, Gleichungsverweis, Formelindex, Formelfaktor, Vorzeichen im `align`-Block, Werkstoffbezeichner, Prozentwert, Symbol) und 2 Tests gegen Fehlalarme („Gleichung“ → „Gl.“, Prüfanmerkungen ⟨…⟩).

## 2. Kennzahlen vorher/nachher (aus `scan_text.py`)

| Text | Wörter | VK Satzlänge | Treffer gesamt | Treffer G≥2 | Nominalis./Satz | Integrität |
|---|---|---|---|---|---|---|
| T1 Physik | 206 → 190 | 0,48 → 0,50 | 9 → 1¹ | 5 → 0 | 1,69 → 1,46 | OK (20/20) |
| T2 Ingenieur | 195 → 169 | 0,42 → 0,45 | 8 → 0 | 6 → 0 | 1,27 → 0,45 | OK (16/16) |
| T3 Floskeln | 199 → 123² | 0,26 → 0,31 | 22 → 1¹ | 16 → 0 | 1,00 → 0,73 | OK (3/3) |
| T4 gut | unverändert | 0,42 | 1 (G1) | 0 | 0,60 | identisch |
| T5 Gleichungen | 165 → 155 | 0,34 → 0,26³ | 2 → 2 | 0 → 0 | 2,50 → 2,33 | OK (20/20) |
| T6 Quellen | 196 → 184 | 0,40 → 0,46 | 5 → 1¹ | 2 → 0 | 1,45 → 1,36 | OK (25/25) |

¹ Verbleibende G1-Treffer sind bewusst belassen (T1: „stets“ im F-markierten Satz; T3: „Auch“-Satz; T6: legitimes „Darüber hinaus“).
² Ohne Prüfanmerkungen ⟨…⟩ gezählt. Der Rückgang beruht fast ausschließlich auf gestrichenen Floskeln.
³ VK sinkt, weil nur der längste Satz (44 → 34 Wörter) gekürzt wurde. In Herleitungen ist das unkritisch, und eine künstliche Variation wäre schlechter (P7).

## 3. Ergebnisse je Testtext

### T1 – Theoretischer Physiktext
- **Geändert (S):** 1.1 E02 → „begrenzt“; 1.2 Hauptsache in Hauptsatz; 3.1 U01+F03 → inhaltlicher Anschluss; 4.1 N08 → Verbalstil; 4.2 Bezug explizit („Nach diesem Kriterium“); 5.2 S04/R04 → Folgerung ausgesprochen.
- **Markiert (F):** 2.3 „stets unabhängig von der Dotierung“ widerspricht $\nu_B = 2 n v_A/\lambda_p$, da $v_A$ zusammensetzungsabhängig ist. 5.2: Verwechslung Faserlänge/$L_{\mathrm{eff}}$.
- **Belassen:** 2.1, 2.2 (Zahlenrechnung geprüft: ≈ 11,15 GHz), 3.2, 3.3, 4.3, 5.1; Hedging „typischerweise“, „in guter Näherung“, „näherungsweise“.
- **Integrität:** 20/20 Elemente unverändert (10 Formeln, 3 Zitate, 1 Gl.-Verweis, Größen, Abkürzung).

### T2 – Ingenieurtext
- **Geändert:** Absatz 1 vollständig (E07, N08 ×2, N01, N02, N03), siehe `examples/paragraph_revision.md`; 3.1 N03 → „wird … gekühlt“; 3.3 R04/N04 → eigener Hauptsatz; 4.1 F05 → „ist … damit“; 4.3 Funktionsverbgefüge → „wird … abgeschätzt“.
- **Belassen:** gesamter Absatz 2 (präzise Zahlenangaben, korrekte Folgerung „somit“: 150 °C − 65 °C = 85 K geprüft); Passiv als Methodikkonvention.
- **Geprüft, nicht markiert:** „Damit unkritisch“ stützt sich auf Tab. 4.1 (nicht im Auszug). Die Folgerung ist plausibel, also kein L-Befund.
- **Integrität:** 16/16 (10 Größen mit Einheit, Zitat [27], Tab. 4.1, Abschnitt 4.4, IGBT, WLTP).

### T3 – Floskeltext
- **Geändert:** alle 5 G3-Treffer (E01, E03, F01, V02, S04) und alle G2-Floskeln (F02 ×2, F03, U02, S01, S05, N05 ×4) entfernt oder ersetzt; R01 „nicht nur … sondern auch“ → einfache Koordination.
- **Markiert:** **F** Photonenenergie/Wellenlänge (Fehler korrekt erkannt und begründet, nicht umgeschrieben); **B** „Studien zeigen“, Zunahme in der Medizintechnik, Attribute „schonend/effizient“; **Autor** Ausblick ohne konkrete Frage.
- **Bewusst nicht gestrichen:** die Triade „präzise, schonende und effiziente“ und die Zunahmebehauptung. Das Entfernen von Sachbehauptungen ist eine Inhaltsentscheidung des Autors, deshalb nur B-Markierung.
- **Offengelegte Inhaltsänderung:** Die Wertungen „unverzichtbar“ und „bahnbrechend“ wurden gestrichen und im Protokoll benannt (Beispiel 14).
- **Kein Herkunftsurteil:** Die Ausgabe benennt Muster sprachlich („Metakommentar ohne Inhalt“), ohne zu behaupten, der Text sei KI-generiert.
- **Integrität:** 3/3 (2,94 µm, Er:YAG, Kapitelnummer).

### T4 – Bereits guter Text
- **Korrektur nach Blindtest:** Der Fließtext bleibt unverändert, erhält aber eine **F-Markierung**. „Verkleinert man den Kernradius, steigt die Intensität“ gilt nach der eigenen Gl. (3.2) nicht für kleine $V$, weil $A_{\mathrm{eff}}$ dort wieder wächst. Der Selbsttest hatte das übersehen, die unabhängige Instanz mit Skill hat es gefunden. Daraus entstand die Regel „Fachliche Gegenprüfung auch bei guten Texten“ in SKILL.md.
- **Ergebnis (sprachlich):** **keine Änderung**. Der einzige Scan-Treffer („maßgeblich“, G1) steht in einem legitimen Kontrastsatz, beide Größen sind eingeführt (Beispiel 7).
- **Begründung für die Rückmeldung:** präzise Gültigkeitsbereiche („für $V$ zwischen 1,2 und 2,4“, „unter 1 %“), Einschränkung der Näherung im letzten Absatz, Hauptsachen in Hauptsätzen, kein Füllwort.
- **Stilkontrolle (Modus K):** Präzision 5 · Natürlichkeit 5 · Terminologie 5 · Grammatik 5 · Satzstruktur 5 · Informationsdichte 5 · Redundanz 5 · Kohärenz 5 · Konsistenz 4 (Hinweis: „Gauß-Funktion“ und „Gauß-Modell“ benennen dasselbe Konzept; beides ist fachüblich, keine Änderung nötig).

### T5 – Gleichungstext
- **Geändert:** nur Satz 1.2 (Schachtelsatz, 44 → 34 Wörter; Einschub verkürzt, Information „Zwischenschritte nicht ausgeführt“ erhalten).
- **Belassen:** „Hierbei bezeichnen“ (U04-Ausnahme), „Damit“ (echte Folgerung, U07), „welcher“ (keine Häufung), die physikalischen Termini („adiabatisch eliminieren“, SVEA).
- **Fachliche Plausibilitätsprüfung:** $\tau_B = 1/\Gamma_B$ mit $\Gamma_B = 2\pi\Delta\nu_B$ und $\Delta\nu_B$ ≈ 20–30 MHz (aus T1) ergibt ≈ 5–8 ns, verträglich mit „etwa 10 ns“. Kein F-Befund.
- **Integrität:** 20/20. Der `align`-Block mit drei `\tag` ist bytegleich (normalisiert ohne Leerzeichen).

### T6 – Fachbegriffe und Quellen
- **Geändert:** 2.3 V02 → Aussage direkt + **B**-Markierung; 2.4 R04 („was die Bedeutung … unterstreicht“) gestrichen; 3.1 N04+F06 → „Neben der Porosität bestimmt …“.
- **Belassen:** 1.1 (E04, aber belegt), 1.3 „wodurch die Duktilität steigt“ (R04-Ausnahme: Sachfolge), 2.1 „Darüber hinaus“ (legitim additiv), alle Zitatsätze im Wortlaut.
- **Integrität:** 25/25 (7 Literaturverweise einschließlich Seitenangabe, Ti-6Al-4V ×2, 10^6 K/s, 800 °C, %-Werte, α' ×3, β, L-PBF ×3, HIP ×2).

## 4. Bewertung der Prüfpunkte

| # | Prüfpunkt | Ergebnis | Nachweis |
|---|---|---|---|
| P1 | Erkennt künstlich wirkende Formulierungen | ✔ | T3: alle 12 erwarteten Mustertypen, 5 G3-Treffer, Signale für Satzlänge und Dreierreihen |
| P2 | Erkennt legitime Standardformulierungen | ✔ | T4 ohne G≥2; T5 „Hierbei bezeichnen“ und „Damit“ belassen; T6 belegtes E04 und einzelnes „Darüber hinaus“ belassen; „Es sei“ in Mathematik G1 |
| P3 | Vermeidet unnötige Synonymersetzungen | ✔ (nach Korrektur) | Selbstprüfung fand einen Verstoß in der eigenen T5-Revision („welcher“ → „der“ ohne Häufung), der rückgängig gemacht wurde |
| P4 | Verbessert Satzbau und Lesbarkeit | ✔ | Treffer G≥2 in allen Texten → 0; Wortzahl −8 % bis −38 %; Nominalisierungen/Satz in T2 1,27 → 0,45 |
| P5 | Fachliche Aussage bleibt erhalten | ✔ | satzweiser Abgleich in `examples/sentence_analysis.md`; Hedging, Gültigkeitsbereiche, Richtungen erhalten; alle F/B nur markiert |
| P6 | Gleichungen und Quellen unverändert | ✔ | 6/6 Revisionen OK; 11/11 Verfälschungen erkannt; 0 Fehlalarme |
| P7 | Kein künstlich vereinheitlichter Stil | ✔ | Passiv in T2, „man“ in T5, Absatzformen unterschiedlich; T5-VK bewusst nicht künstlich erhöht |
| P8 | Guter Text bleibt unverändert | ✔ | T4-Fließtext wortgleich mit Original (nur F-Markierung ergänzt); im Blindtest ebenso, ohne Skill dagegen Ähnlichkeit 0,85 |

## 5. Während der Tests gefundene Schwächen und Verbesserungen

| # | Schwäche | Gefunden in | Korrektur |
|---|---|---|---|
| 1 | „(engl. …)“ trennte einen Satz | T6-Scan | Abkürzungsliste um engl., lat., bzgl., ff. u. a. erweitert |
| 2 | Doppelmeldungen (F01 + F02 auf demselben Text; E02 + N06 „zentrale“) | T3, T1 | Überlappungsregel: Teiltreffer oder gleichkategoriale Überlappung wird unterdrückt |
| 3 | E02 verpasste „spielen Lasertechnologien eine immer größere Rolle“ | T3 | Regex erlaubt bis zu 8 Wörter zwischen Verb und „Rolle“ |
| 4 | N08 verpasste Inversion „erfolgt die Durchführung“ | T2 | zweite Regex-Alternative |
| 5 | S04 verpasste „was die Bedeutung … unterstreicht“ | T1, T6 | umgekehrte Wortfolge ergänzt |
| 6 | V02 hätte auch belegte Zuschreibungen gemeldet | Entwurf | V02 entfällt, wenn im Satz ein Literaturverweis steht |
| 7 | Integrität: „Ti-6Al-4V“ als Größe „4 V“, „10^6 K/s“ als „6 K/s“, „L-PBF“ als „PBF“, „8 l/min“ als „8 l“ | T6, T2 | Kategorie „Bezeichner“; Zehnerpotenzen; Bindestrich-Akronyme; Einheiten mit /min |
| 8 | Integrität: Prüfanmerkungen ⟨…⟩ mit Formeln erzeugten Fehlalarme | T1-Revision | Anmerkungen werden ignoriert (dokumentiert in SKILL.md) |
| 9 | Scan zählte „Studien zeigen“ in einer B-Anmerkung als Floskel | T3-Revision (Testfehlschlag) | Anmerkungen werden auch im Scan ignoriert |
| 10 | N02 meldete normale zweistufige Genitive („der Dotierung des Faserkerns“) | T1 (Fehlalarm) | nur noch dreistufige Ketten; Artikel am Satzanfang großschreibungstolerant |
| 11 | Eigene Revision tauschte „welcher“ → „der“ ohne Grund | Selbstprüfung T5 | rückgängig gemacht; Regel in `sentence_structures.md` §5 präzisiert |

## 6. Bekannte Grenzen
- Logische (L) und fachliche (F) Probleme erkennt nur das Lesen, nicht der Scan. Der Scan liefert für F nur Kandidaten (V04, F08).
- Die Gewichte G1–G3 und die Scan-Schwellen sind heuristisch und an sechs kurzen Texten kalibriert. Bei sehr kurzen Texten (unter 8 Sätzen) sind die Statistiksignale nicht aussagekräftig.
- `check_integrity.py` vergleicht Multimengen. Es erkennt veränderte, fehlende und neue Elemente, aber nicht, ob ein Verweis in einen anderen Satz gewandert ist. Das prüft Schritt 7 von Hand.
- Ausgeschriebene Zahlen („zwei Proben“) und Fachbegriffe ohne `--terms`-Liste werden nicht automatisch geschützt.
- Der Blindtest lief mit Instanzen desselben Modells. Eine Prüfung durch einen menschlichen Fachlektor steht aus.
