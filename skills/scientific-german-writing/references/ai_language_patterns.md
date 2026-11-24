# Bibliothek: KI-typische und künstlich wirkende Formulierungsmuster

## Inhalt
0. Status, Belege und Gebrauch dieser Bibliothek
1. E – Einleitungen (E01–E07)
2. U – Übergänge (U01–U07)
3. S – Schlussformulierungen (S01–S06)
4. F – Floskeln und Metakommentare (F01–F08)
5. N – Überhöhte Sprache (N01–N08)
6. R – Satzschablonen (R01–R08)
7. V – Vagheit und Hedging (V01–V05)
8. A – Argumentationsschablonen (A01–A06), nur durch Lesen erkennbar
9. Kurzübersicht: Prüffragen

---

## 0. Status, Belege und Gebrauch

**Was belegt ist.** Studien zu englischsprachigen Texten zeigen, dass Sprachmodelle bestimmte Wörter überproportional verwenden: Kobak et al. 2025 untersuchen 15 Mio. PubMed-Abstracts, Juzek & Ward 2025 die Wörter rund um „delve“. Instruktionsoptimierte Modelle nutzen Nominalisierungen etwa 1,5- bis 2-mal und Partizipialkonstruktionen deutlich häufiger als Menschen (Reinhart et al. 2025, PNAS). Der Wikipedia-Leitfaden „Signs of AI writing“ dokumentiert aus redaktioneller Praxis unter anderem überhöhte Bedeutungszuschreibungen, vage Zuschreibungen, negative Parallelismen („nicht nur … sondern“), Dreierreihen, Vermeidung von „ist“ („serves as“) und schematische Schlüsse. Belege stehen in `source_references.md`.

**Was eigene Ableitung ist.** Die deutschen Entsprechungen, die Gewichte G1–G3 und die Häufigkeitsangaben unten sind **eigene, nachvollziehbar begründete Übertragungen**. Sie beruhen auf den genannten Studien, auf deutschen Schreibratgebern (Floskeln, Funktionsverbgefüge, Blähverben: Mainz, Mannheim) und auf typischen Lehnübersetzungen englischer Modellformulierungen. Für das Deutsche gibt es nach unserer Recherche (Stand 11/2026) keine vergleichbar große Korpusstudie. Die Angaben sind daher als begründete Arbeitshypothesen zu verstehen.

**Was nicht geht.** Kein einzelnes Muster und keine Kombination beweist eine KI-Herkunft. Menschen schreiben diese Formulierungen ebenfalls, denn Modelle haben sie von Menschen gelernt. Detektoren sind unzuverlässig (Weber-Wulff et al. 2023; Sadasivan et al. 2023) und benachteiligen Nichtmuttersprachler (Liang et al. 2023). Diese Bibliothek bewertet deshalb ausschließlich die **sprachliche Leistung** einer Formulierung.

**Gebrauch.** Jeder Eintrag enthält: Muster · Kategorie · typischer Kontext · wissenschaftliche Eignung · häufige Schwäche · Erklärung · Strategie · Alternativen · Beispiel · Ausnahmen. Die Bewertung jedes Musters umfasst **Häufigkeit** (wie oft es in generierten Fachtexten typischerweise auffällt: hoch/mittel/gering), **Kontextabhängigkeit** (wie oft es legitim ist: hoch = oft legitim) und **Problemgehalt** (G1 = meist legitim, nur Häufung prüfen; G2 = oft entbehrlich; G3 = fast immer inhaltsleer).

---

## 1. E – Einleitungen

### E01 – Zeitgeist-Einstieg: „In der heutigen (schnelllebigen/digitalen) Welt …“
- **Kategorie:** Einleitung · Häufigkeit: hoch · Kontextabhängigkeit: gering · **G3**
- **Kontext:** erster Satz einer Einleitung oder eines Kapitels.
- **Eignung:** ungeeignet. Die Aussage ist unprüfbar, ohne Zeitbezug und ohne Fachbezug.
- **Schwäche:** Der Satz verzögert den Gegenstand und behauptet eine allgemeine Entwicklung ohne Beleg.
- **Strategie:** streichen und mit dem Gegenstand, dem Problem oder einer belegten Zahl beginnen.
- **Alternativen:** „<Gegenstand> wird eingesetzt für …“ · „Ein ungelöstes Problem bei … ist …“ · „Seit <Jahr/Ereignis> …“ (mit Beleg).
- **Beispiel:** „In der heutigen schnelllebigen Welt spielen Laser eine immer größere Rolle in der Medizintechnik.“ → „Laser werden in der Medizintechnik unter anderem zum Schneiden, Abtragen und Koagulieren von Gewebe eingesetzt.“ (nur, wenn diese Anwendungen im Text stehen; sonst: „Laser werden in der Medizintechnik zur Gewebebearbeitung eingesetzt.“)
- **Ausnahme:** Historische Einordnung mit konkretem Zeitbezug und Beleg („Seit der Einführung der EUV-Lithografie 2019 …“).

### E02 – „X spielt eine zentrale/entscheidende/wichtige Rolle bei Y“
- **Kategorie:** Einleitung/Bedeutungszuschreibung · Häufigkeit: sehr hoch · Kontextabhängigkeit: mittel · **G2**
- **Kontext:** Themeneinführung, Begründung der Relevanz.
- **Eignung:** bedingt. Die Wendung ist idiomatisch, sagt aber nicht, **welche** Rolle X hat.
- **Schwäche:** Platzhalter für eine fehlende Funktionsangabe; oft mit Intensivierer (N06).
- **Strategie:** die konkrete Funktion aus dem Kontext als Verb einsetzen. Gibt der Text sie nicht her, belassen oder als zu vage markieren.
- **Alternativen:** „X begrenzt / bestimmt / steuert / verursacht / ermöglicht Y“ · „Y hängt von X ab“ · „X ist der dominierende Verlustmechanismus bei Y“.
- **Beispiel:** „SBS spielt eine zentrale Rolle bei der Leistungsskalierung schmalbandiger Faserlaser.“ → „SBS begrenzt die Leistungsskalierung schmalbandiger Faserlaser.“ (zulässig, weil der folgende Text die Schwelle als Begrenzung beschreibt).
- **Ausnahme:** Wenn die Rolle anschließend ausdrücklich erklärt wird, darf der Satz als Ankündigung stehen bleiben. Einmal im Text ist unauffällig.

### E03 – „X ist ein faszinierendes/vielschichtiges/spannendes Forschungsfeld“
- **Kategorie:** Einleitung/Wertung · Häufigkeit: mittel · Kontextabhängigkeit: gering · **G3**
- **Eignung:** ungeeignet, weil die Wertung subjektiv ist (Mainz: emotionale Wertungen vermeiden).
- **Strategie:** streichen. Wenn Komplexität gemeint ist, die Komponenten nennen.
- **Alternativen:** „X umfasst A, B und C“ · „X ist noch nicht vollständig verstanden, insbesondere …“
- **Beispiel:** „Die Laserablation ist ein faszinierendes Forschungsfeld, das …“ → „Bei der Laserablation …“
- **Ausnahme:** Populärwissenschaftliche Textsorten, aber nicht in Abschlussarbeiten.

### E04 – „X hat in den letzten Jahren zunehmend an Bedeutung gewonnen“
- **Kategorie:** Einleitung · Häufigkeit: hoch · Kontextabhängigkeit: mittel · **G2**
- **Eignung:** nur mit Beleg (Publikationszahlen, Marktdaten, Normen).
- **Schwäche:** Die Entwicklung wird ohne Beleg behauptet, der Zeitraum bleibt vage.
- **Strategie:** belegen oder streichen. Fehlt der Beleg, als **B** markieren.
- **Alternativen:** „Die Zahl der Veröffentlichungen zu X hat sich zwischen 2015 und 2023 verdreifacht [n].“ · „X wird seit <Jahr> in <Anwendung> eingesetzt [n].“
- **Ausnahme:** Belegter Satz mit Quelle, z. B. „hat sich … zunehmend etabliert (Weber et al., 2019)“, ist legitim.

### E05 – Übertriebene Ankündigung: „wird umfassend beleuchtet/eingehend erörtert“
- **Kategorie:** Einleitung/Metatext · Häufigkeit: hoch · Kontextabhängigkeit: mittel · **G2**
- **Schwäche:** „beleuchten“ ist eine Metapher; „umfassend“ verspricht mehr, als der Abschnitt meist hält.
- **Strategie:** die tatsächliche Tätigkeit nennen (herleiten, messen, vergleichen, abschätzen).
- **Alternativen:** „Kapitel 3 leitet … her.“ · „Abschnitt 4.2 vergleicht … mit …“ · „Im Folgenden wird … abgeschätzt.“
- **Beispiel:** „In diesem Kapitel werden die Grundlagen der SBS umfassend beleuchtet.“ → „Dieses Kapitel beschreibt die Grundlagen der SBS, soweit sie für die Schwellabschätzung in Kapitel 4 nötig sind.“ (Zweck nur nennen, wenn er bekannt ist.)
- **Ausnahme:** Kapitelvorschau in Einleitungen ist üblich, aber ohne Intensivierer.

### E06 – „Um X zu verstehen, ist es zunächst wichtig, Y zu betrachten“
- **Kategorie:** Einleitung/Überleitung · Häufigkeit: hoch · Kontextabhängigkeit: gering · **G3**
- **Schwäche:** Der Satz kündigt nur an, dass Y folgt, und verzögert die Information.
- **Strategie:** direkt mit Y beginnen. Die Abhängigkeit, falls nötig, als Begründung formulieren.
- **Alternativen:** „X beruht auf Y.“ · „Grundlage für X ist Y.“
- **Beispiel:** „Um die Brillouin-Streuung zu verstehen, ist es wichtig, zunächst akustische Wellen in Glas zu betrachten.“ → „Die Brillouin-Streuung beruht auf der Wechselwirkung von Licht mit akustischen Wellen im Glas.“

### E07 – „Im Rahmen der vorliegenden Arbeit …“
- **Kategorie:** Einleitung/Metatext · Häufigkeit: hoch (auch bei Menschen) · Kontextabhängigkeit: hoch · **G1**
- **Eignung:** in Einleitung, Zielsetzung und Methodik legitim.
- **Schwäche:** im laufenden Text redundant, oft verbunden mit Blähverb („erfolgt im Rahmen … die Durchführung“).
- **Strategie:** im Fließtext streichen, in der Zielsetzung belassen.
- **Beispiel:** „Im Rahmen der vorliegenden Arbeit erfolgt die Durchführung der thermischen Auslegung auf Grundlage eines Cauer-Netzwerks.“ → „Das Modul wird auf Grundlage eines Cauer-Netzwerks thermisch ausgelegt.“

---

## 2. U – Übergänge

### U01 – Additive Konnektoren: „Darüber hinaus / Des Weiteren / Zudem / Außerdem / Ferner“
- **Kategorie:** Übergang · Häufigkeit: sehr hoch · Kontextabhängigkeit: **hoch** · **G1**
- **Eignung:** legitim, wenn eine **neue, gleichrangige** Information zum selben Thema folgt.
- **Schwäche:** Der Konnektor wird mechanisch an jeden Absatzanfang gesetzt, oder die Relation ist gar nicht additiv (Folgerung, Gegensatz, Präzisierung).
- **Strategie:** (1) Relation bestimmen (siehe `transitions_and_connectors.md`). (2) Ist sie additiv und durch die Reihenfolge klar, den Konnektor streichen. (3) Ist sie nicht additiv, den passenden Konnektor wählen. (4) Bei Häufung variieren **nur durch Streichen oder Präzisieren**, nicht durch ein Synonymkarussell.
- **Alternativen:** Konnektor weglassen · thematischer Anschluss über das Subjekt („Die Bandbreite des Gewinnspektrums …“) · „Neben A bestimmt auch B …“ · „Ein zweiter Verlustmechanismus ist …“
- **Beispiel:** „Darüber hinaus ist die Bandbreite des Brillouin-Gewinnspektrums von besonderer Bedeutung.“ → „Neben der Frequenzverschiebung charakterisiert die Bandbreite das Brillouin-Gewinnspektrum.“
- **Ausnahme:** Einmalig in einem Absatz, der tatsächlich einen weiteren Punkt hinzufügt: **belassen**. Beispiel T6: „Darüber hinaus weisen L-PBF-Bauteile prozessbedingt Porosität auf.“ Hier folgt ein zweiter, gleichrangiger Werkstoffaspekt, also wird belassen.

### U02 – „In diesem Zusammenhang …“
- **Kategorie:** Übergang · Häufigkeit: hoch · Kontextabhängigkeit: mittel · **G2**
- **Schwäche:** behauptet einen Zusammenhang, ohne ihn zu benennen (Ursache? Beispiel? Bedingung?).
- **Strategie:** die Relation explizit machen oder streichen.
- **Alternativen:** „Deshalb …“ · „Ein Beispiel dafür ist …“ · „Unter dieser Bedingung …“ · „Dazu passt, dass …“ · Relativanschluss.
- **Beispiel:** „In diesem Zusammenhang ist anzumerken, dass Wasser bei 2,94 µm ein Absorptionsmaximum aufweist.“ → „Wasser hat bei 2,94 µm ein ausgeprägtes Absorptionsmaximum.“
- **Ausnahme:** Wenn der vorige Satz den Zusammenhang genau benennt und der Bezug eindeutig ist.

### U03 – „Vor diesem Hintergrund …“
- **Kategorie:** Übergang · Häufigkeit: mittel · Kontextabhängigkeit: hoch · **G1**
- **Eignung:** legitim vor einer Folgerung oder Zielsetzung, die aus dem zuvor Beschriebenen motiviert ist.
- **Schwäche:** Bei Häufung oder ohne erkennbaren „Hintergrund“ wirkt es schablonenhaft.
- **Strategie:** einmal pro Abschnitt belassen; sonst „Daher …“ oder „Ziel dieser Arbeit ist deshalb …“.

### U04 – „Dabei / Hierbei / Hierzu / Diesbezüglich“ als Universalanschluss
- **Kategorie:** Übergang/Bezug · Häufigkeit: hoch · Kontextabhängigkeit: hoch · **G1**
- **Eignung:** „Dabei“ ist idiomatisch für Begleitumstände oder Erläuterungen von Symbolen („Hierbei bezeichnet …“).
- **Schwäche:** Der Bezug ist unklar (wobei genau?); in Serie wirkt es monoton.
- **Strategie:** den Bezug prüfen. Bei mehreren möglichen Bezugspunkten ein Nomen setzen („Bei diesem Kriterium …“).
- **Ausnahme:** Variablenerklärung nach Formeln („Hierbei bezeichnen $A_p$ und $A_s$ …“) ist Standard und wird **belassen**.

### U05 – Vorschau-Überleitung: „Im Folgenden wird … näher betrachtet“
- **Kategorie:** Übergang/Metatext · Häufigkeit: hoch · Kontextabhängigkeit: hoch · **G1**
- **Eignung:** am Kapitel- oder Abschnittsanfang legitim und leserfreundlich.
- **Schwäche:** innerhalb eines Abschnitts vor jedem Absatz; „näher“ ohne Bezugspunkt.
- **Strategie:** belassen, wo eine Struktur angekündigt wird; streichen, wo der nächste Satz ohnehin folgt.

### U06 – Rückblick + Vorschau: „Nachdem nun X betrachtet wurde, wenden wir uns Y zu“
- **Kategorie:** Übergang · Häufigkeit: mittel · Kontextabhängigkeit: mittel · **G2**
- **Schwäche:** Der Satz wiederholt Bekanntes und verbraucht einen Satz ohne Information.
- **Strategie:** durch einen inhaltlichen Anschluss ersetzen: Warum folgt Y aus X?
- **Alternativen:** „Die Schwellleistung aus Gl. (2.8) setzt eine bekannte Gewinnbandbreite voraus. Diese hängt …“
- **Ausnahme:** Zwischen Großkapiteln einer Dissertation ist eine knappe Brücke üblich.

### U07 – Konklusive Konnektoren: „Somit / Damit / Folglich / Daher“
- **Kategorie:** Übergang/Logik · Häufigkeit: hoch · Kontextabhängigkeit: hoch · **G1**
- **Eignung:** notwendig, wenn tatsächlich gefolgert wird.
- **Schwäche:** Der Satz folgt nicht aus dem Vorherigen (Scheinkausalität, **Klasse L**).
- **Strategie:** prüfen, ob der Vordersatz die Folgerung trägt. Wenn nicht, den Konnektor streichen oder die fehlende Prämisse markieren.
- **Beispiel (L):** „Die Messung ergab 0,11 K/W. Somit ist das Modul für alle Betriebszustände geeignet.“ → Markieren: ⟨L: Folgt nur für den Nennbetriebspunkt; transiente Lasten nicht betrachtet.⟩

---

## 3. S – Schlussformulierungen

### S01 – „Zusammenfassend lässt sich sagen/festhalten, dass …“
- **Kategorie:** Schluss · Häufigkeit: sehr hoch · Kontextabhängigkeit: mittel · **G2**
- **Eignung:** legitim am Kapitelende, wenn tatsächlich verdichtet wird; dann ist „Zusammenfassend“ ein nützliches Signalwort.
- **Schwäche:** am Absatzende oder in kurzen Texten; die „Zusammenfassung“ wiederholt nur oder verallgemeinert ins Leere.
- **Strategie:** prüfen, ob eine echte Verdichtung folgt. Wenn ja, das kürzere „Zusammengefasst: …“ verwenden oder die Wendung belassen. Wenn nein, streichen.
- **Beispiel:** „Zusammenfassend lässt sich sagen, dass die Laserablation ein vielschichtiges Zusammenspiel physikalischer, biologischer und technischer Faktoren darstellt.“ → streichen oder konkret machen: „Der Ablationserfolg hängt damit von Wellenlänge, Pulsdauer und Pulsenergie sowie von der Wasserabsorption des Gewebes ab.“ (nur Faktoren, die im Text vorkommen)

### S02 – „Abschließend lässt sich feststellen, dass …“
- Wie S01 · **G2** · Ersetzen durch die Feststellung selbst. Am Arbeitsende im Fazit legitim.

### S03 – „Insgesamt zeigt sich, dass …“
- **Kategorie:** Schluss/Ergebnis · Häufigkeit: hoch · Kontextabhängigkeit: mittel · **G2**
- **Schwäche:** wiederholt Einzelergebnisse als vage Gesamtaussage.
- **Strategie:** das konkrete Gesamtergebnis mit Bezug nennen: „Alle drei Proben erreichen …“.

### S04 – „Dies unterstreicht/verdeutlicht die Bedeutung von …“
- **Kategorie:** Schluss/Bedeutungszuschreibung · Häufigkeit: sehr hoch · Kontextabhängigkeit: gering · **G3**
- **Schwäche:** Bedeutung wird behauptet statt gezeigt; „Dies“ hat oft keinen klaren Bezug (R08).
- **Strategie:** die konkrete Konsequenz formulieren oder streichen.
- **Alternativen:** „Für Hochleistungsanwendungen werden deshalb möglichst kurze Fasern eingesetzt.“ (wenn im Text belegt) · „Die Parameterwahl muss daher … berücksichtigen.“
- **Beispiel:** „Gleichung (2.8) verdeutlicht, dass die Schwelle mit zunehmender Faserlänge sinkt, was die Bedeutung kurzer Fasern für Hochleistungsanwendungen unterstreicht.“ → „Nach Gleichung (2.8) sinkt die Schwelle mit zunehmender effektiver Länge; für hohe Leistungen sind daher kurze Fasern günstig.“ (Hinweis: Die Gleichung enthält $L_{\mathrm{eff}}$, nicht die Faserlänge. Das ist eine **F**-Präzisierung und muss im Protokoll begründet werden.)

### S05 – Ausblick-Floskel: „Zukünftige Forschung sollte … weiter untersuchen“
- **Kategorie:** Schluss/Ausblick · Häufigkeit: hoch · Kontextabhängigkeit: mittel · **G2**
- **Schwäche:** unspezifisch, ohne offene Frage, Methode oder Hypothese.
- **Strategie:** eine konkrete offene Frage nennen, sofern der Text sie hergibt; sonst streichen oder den Autor fragen.
- **Beispiel:** „Zukünftige Forschung sollte diese Aspekte weiter untersuchen, um das volle Potenzial … auszuschöpfen.“ → ⟨Autor: Welche offene Frage genau? Z. B. Einfluss der Repetitionsrate auf die thermische Schädigung?⟩

### S06 – Absatzend-Resümee: „Somit wird deutlich, dass …“
- **Kategorie:** Schluss · Häufigkeit: hoch · Kontextabhängigkeit: mittel · **G2**
- **Schwäche:** Jeder Absatz endet mit einer Wiederholung. Das ist ein bekanntes Strukturmerkmal generierter Texte (Wikipedia: „section-ending summaries“).
- **Strategie:** streichen, wenn der Satz nur wiederholt; behalten, wenn er eine Folgerung zieht, die für den nächsten Absatz gebraucht wird.

---

## 4. F – Floskeln und Metakommentare

### F01 – „Es ist wichtig zu beachten/betonen, dass …“ (engl. *It is important to note that*)
- **Kategorie:** Floskel · Häufigkeit: sehr hoch · Kontextabhängigkeit: gering · **G3**
- **Eignung:** ungeeignet; ein Metakommentar ersetzt die Begründung.
- **Schwäche:** Die Wichtigkeit wird behauptet, nicht begründet; der Satz verlängert sich ohne Information.
- **Strategie:** (a) streichen und den dass-Satz zum Hauptsatz machen; (b) wenn die Wichtigkeit Teil der Aussage ist, den **Grund** nennen.
- **Alternativen:** Aussage direkt · „X ist entscheidend für Y, weil …“ · „Zu beachten ist dabei: …“ (nur in Anleitungen oder Methodik)
- **Beispiel:** „Es ist wichtig zu beachten, dass die Wahl der Wellenlänge, die Pulsdauer und die Pulsenergie entscheidende Faktoren für den Behandlungserfolg sind.“ → „Der Behandlungserfolg hängt von Wellenlänge, Pulsdauer und Pulsenergie ab.“
- **Ausnahme:** Warnhinweise in Methodenteilen („Wichtig: Die Probe muss vor der Messung …“). Dort trägt die Wichtigkeit Handlungsinformation.

### F02 – „Es ist hervorzuheben/anzumerken/festzuhalten, dass …“, „In diesem Zusammenhang ist anzumerken …“
- **Kategorie:** Floskel · Häufigkeit: hoch · Kontextabhängigkeit: mittel · **G2**
- **Schwäche:** wie F01; oft Kette aus U02 + F02.
- **Strategie:** streichen. Soll gewichtet werden, die Gewichtung inhaltlich begründen („Entscheidend für die Wahl des Er:YAG-Lasers ist, dass …“).
- **Ausnahme:** „Festzuhalten ist …“ als Zwischenfazit nach langer Herleitung, einmalig.

### F03 – „Von besonderer Bedeutung ist …“
- **Kategorie:** Floskel/Wertung · Häufigkeit: hoch · Kontextabhängigkeit: mittel · **G2**
- **Schwäche:** Bedeutung ohne Bezugsgröße: wofür bedeutsam?
- **Strategie:** Bezug nennen oder streichen.
- **Beispiel:** „Von besonderer Bedeutung ist dabei, dass Er:YAG-Laser genau bei dieser Wellenlänge emittieren …“ → „Er:YAG-Laser emittieren bei 2,94 µm und damit im Absorptionsmaximum von Wasser.“

### F04 – „Es sei darauf hingewiesen, dass …“ / „Es sei …“
- **Kategorie:** Floskel/Konvention · Häufigkeit: mittel · Kontextabhängigkeit: **hoch** · **G1**
- **Eignung:** In Mathematik und theoretischer Physik ist der Konjunktiv-I-Gebrauch („Es sei $f$ stetig“, „Es sei bemerkt“) etablierte Konvention.
- **Schwäche:** nur bei Häufung (mehr als einmal pro Seite).
- **Strategie:** Mathematische Setzungen („Es sei …“) **immer belassen**; Hinweis-Floskeln bei Häufung kürzen („Bemerkung: …“ oder direkt).

### F05 – „Es lässt sich feststellen/erkennen, dass …“, „Es zeigt sich, dass …“
- **Kategorie:** Floskel · Häufigkeit: hoch · Kontextabhängigkeit: mittel · **G2**
- **Schwäche:** Der eigentliche Inhalt steht im Nebensatz; die Evidenzquelle (wo zeigt es sich?) fehlt.
- **Strategie:** dass-Satz zum Hauptsatz machen und Evidenz ergänzen, sofern sie im Text steht („Die Messung zeigt …“, „Aus Tab. 4.1 folgt …“).
- **Beispiel:** „Es zeigt sich, dass das Modul im Nennbetrieb thermisch unkritisch ist.“ → „Im Nennbetrieb ist das Modul damit thermisch unkritisch.“
- **Ausnahme:** „Es zeigt sich“ nach einer Darstellung von Messdaten ist legitim, wenn der Bezug klar ist.

### F06 – „Ein wesentlicher Aspekt/Faktor ist …“
- **Kategorie:** Floskel/Platzhalter · Häufigkeit: hoch · Kontextabhängigkeit: mittel · **G2**
- **Schwäche:** „Aspekt“ oder „Faktor“ ersetzt die Benennung des Gegenstands; meist mit N04 („stellt … dar“) kombiniert.
- **Strategie:** Gegenstand plus Wirkung direkt: „Die Oberflächenrauheit verringert die Ermüdungsfestigkeit.“
- **Ausnahme:** „Faktor“ als Fachbegriff (Gütefaktor, Füllfaktor, Formfaktor) ist unberührt.

### F07 – „Nicht zuletzt …“
- **Kategorie:** Floskel/Gewichtung · Häufigkeit: mittel · Kontextabhängigkeit: mittel · **G2**
- **Strategie:** belassen nur, wenn der letzte Punkt tatsächlich besonders wichtig ist und das begründet wird; sonst streichen.

### F08 – Evidenzbehauptung ohne Beleg: „bekanntlich / selbstverständlich / offensichtlich / zweifellos“
- **Kategorie:** Floskel/Beleg · Häufigkeit: mittel · Kontextabhängigkeit: mittel · **G2**
- **Schwäche:** markiert eine Aussage als unbestritten und entzieht sie so der Prüfung.
- **Strategie:** Ist die Aussage Fachstandard (Lehrbuchwissen), das Adverb streichen. Ist sie nicht trivial, **B** markieren.
- **Ausnahme:** „bekanntlich“ vor einem klassischen Lehrbuchresultat mit Verweis.

---

## 5. N – Überhöhte Sprache

### N01 – Funktionsverbgefüge: „eine Analyse durchführen“, „zur Anwendung kommen“, „in Betracht ziehen“
- **Kategorie:** Nominalstil · Häufigkeit: hoch · Kontextabhängigkeit: **hoch** · **G1**
- **Eignung:** Viele Gefüge sind fachlich etabliert („eine Messung durchführen“, „in Betrieb nehmen“) oder nuancieren den Aspekt („zur Verfügung stehen“). Mannheim und Mainz empfehlen, sie aufzulösen, **wo ein einfaches Verb dasselbe leistet**.
- **Strategie:** auflösen, wenn ein einfaches Verb dieselbe Bedeutung hat; belassen, wenn das Gefüge Terminus oder Aspekt trägt.
- **Alternativen:** zur Anwendung kommen → angewendet werden; eine Einteilung vornehmen → einteilen; Einfluss haben auf → beeinflussen; einer Prüfung unterziehen → prüfen; Berücksichtigung finden → berücksichtigt werden.
- **Beispiel:** „…, wobei die Bestimmung der Schaltverluste anhand der Datenblattangaben zur Anwendung kommt.“ → „Die Schaltverluste werden aus den Datenblattangaben bestimmt.“

### N02 – Nominal- und Genitivketten
- **Kategorie:** Nominalstil · Häufigkeit: hoch · Kontextabhängigkeit: hoch · **G2**
- **Schwäche:** Ketten wie „die Ermittlung der Verlustleistung der Halbleiterschalter“ erzwingen Blähverben und verstecken das Agens (Mainz). Instruktionsoptimierte Modelle nominalisieren messbar häufiger als Menschen (Reinhart et al. 2025).
- **Strategie:** das Kopfnomen in ein Verb verwandeln; **Fachkomposita und feste Termini als Einheit erhalten** („Dämpfung der akustischen Phononen“ ist Fachsprache).
- **Beispiel:** „Die Ermittlung der Verlustleistung der Halbleiterschalter findet unter Berücksichtigung der Schalt- und Durchlassverluste statt.“ → „Die Verlustleistung der Halbleiterschalter setzt sich aus Schalt- und Durchlassverlusten zusammen.“ (Bedeutungsprüfung: „unter Berücksichtigung“ heißt hier „beide Anteile werden einbezogen“, das ist gleichwertig.)
- **Ausnahme:** Definitionen und Überschriften dürfen nominal sein.

### N03 – Blähverben: „erfolgt / findet statt / vollzieht sich“
- **Kategorie:** Nominalstil · Häufigkeit: hoch · Kontextabhängigkeit: mittel · **G1**
- **Schwäche:** Das Verb trägt keine Bedeutung, die Handlung steckt im Nomen (Mainz: „Blähverben“).
- **Strategie:** das Nomen zum Verb machen.
- **Beispiel:** „Die Kühlung des Moduls erfolgt über eine Pin-Fin-Kühlplatte.“ → „Das Modul wird über eine Pin-Fin-Kühlplatte gekühlt.“
- **Ausnahme:** Wenn das Nomen Terminus ist und kein gutes Verb existiert („Die Zündung erfolgt bei …“ ist in Verbrennungsmotorik üblich).

### N04 – Kopula-Vermeidung: „stellt … dar“, „fungiert als“, „dient als“ (engl. *serves as*)
- **Kategorie:** Überhöhung · Häufigkeit: hoch · Kontextabhängigkeit: mittel · **G1**
- **Schwäche:** gehobene Umschreibung für „ist“ (Wikipedia: *avoidance of basic copulatives*).
- **Strategie:** „ist“ oder ein inhaltliches Verb.
- **Beispiel:** „Die Oberflächenrauheit stellt einen weiteren entscheidenden Faktor für die Ermüdungsfestigkeit dar.“ → „Auch die Oberflächenrauheit beeinflusst die Ermüdungsfestigkeit.“ (Die Richtung „verringert“ steht nur dann, wenn der Text sie belegt.)
- **Ausnahme:** „Abb. 3 stellt … dar“ (Darstellung im Wortsinn); „dient als Referenz“ (Funktion).

### N05 – Gehobene Modewörter und Metaphern: „beleuchten, entfalten, nahtlos, vielschichtig, Zusammenspiel, Wechselspiel, Schlüsselrolle, Meilenstein, bahnbrechend, unverzichtbar, Landschaft“
- **Kategorie:** Überhöhung · Häufigkeit: hoch · Kontextabhängigkeit: gering · **G2**
- **Schwäche:** werbend oder metaphorisch, ohne messbaren Gehalt; entspricht den englischen Überrepräsentationen (*delve, tapestry, intricate, pivotal, landscape*; Kobak et al. 2025; Juzek & Ward 2025).
- **Strategie:** Fachbegriff oder konkrete Beschreibung; Wertungen streichen.
- **Beispiel:** „…, was sie zu einem unverzichtbaren Werkzeug in der Zahnmedizin macht.“ → „Er:YAG-Laser werden deshalb in der Zahnmedizin und Dermatologie eingesetzt.“ (Die Wertung „unverzichtbar“ entfällt. Soll sie bleiben, braucht sie einen Beleg.)
- **Ausnahme:** „Wechselwirkung“ ist Fachbegriff, nicht „Wechselspiel“; „Meilenstein“ im Projektmanagement.

### N06 – Intensivierer und Wertadjektive: „entscheidend, maßgeblich, essenziell, fundamental, erheblich, robust, umfassend, effizient, innovativ“
- **Kategorie:** Überhöhung · Häufigkeit: sehr hoch · Kontextabhängigkeit: **hoch** · **G1**
- **Schwäche:** Wertung ohne Maßstab; Häufung inflationiert die Wertung.
- **Strategie:** quantifizieren (Zahl, Vergleich) oder streichen. „maßgeblich“ in Kontrastsätzen („nicht A, sondern B ist maßgeblich“) ist präzise und wird **belassen**.
- **Ausnahme:** Fachtermini („effizient“ als Wirkungsgrad, „robust“ in Regelungstechnik, „signifikant“ statistisch).

### N07 – Anglizismen und Lehnübersetzungen: „Sinn machen“, „in 2020“, „adressieren“, „mit anderen Worten“, „signifikant“ (= deutlich)
- **Kategorie:** Überhöhung/Interferenz · Häufigkeit: mittel · Kontextabhängigkeit: mittel · **G2**
- **Strategie:** „Sinn ergeben“, „im Jahr 2020“/„2020“, „behandeln/angehen/lösen“, „das heißt“, „deutlich“; „signifikant“ nur mit statistischem Test.
- **Ausnahme:** etablierte Fachanglizismen (Pulse Shaping, Keyhole, Lock-in) bleiben.

### N08 – Blähnomen + Blähverb: „Die Durchführung/Ermittlung/Bestimmung … erfolgt/findet statt“
- **Kategorie:** Nominalstil · Häufigkeit: hoch · Kontextabhängigkeit: gering · **G2**
- **Schwäche:** doppelte Leere: Weder das Nomen („Durchführung“) noch das Verb („erfolgt“) trägt Inhalt.
- **Strategie:** das Verb aus dem inhaltlichen Nomen bilden.
- **Beispiel:** „Die Durchführung einer Abschätzung der Schwellleistung erfolgt üblicherweise mit dem Kriterium nach Smith [14].“ → „Die Schwellleistung wird üblicherweise mit dem Kriterium nach Smith [14] abgeschätzt.“

---

## 6. R – Satzschablonen

### R01 – „nicht nur …, sondern auch …“ / „sowohl … als auch …“
- **Kategorie:** Satzschablone · Häufigkeit: hoch · Kontextabhängigkeit: hoch · **G1**
- **Eignung:** legitim, wenn der zweite Teil **überraschend** über den ersten hinausgeht.
- **Schwäche:** wiederholt eingesetzt als rhetorische Steigerung ohne Kontrast (Wikipedia: *negative parallelisms*).
- **Strategie:** bei Häufung durch einfache Koordination ersetzen („A und B“), wenn kein Kontrast gemeint ist.
- **Beispiel:** „…, das nicht nur die Präzision chirurgischer Eingriffe erhöht, sondern auch neue Therapieansätze ermöglicht.“ → „…, das die Präzision chirurgischer Eingriffe erhöht und neue Therapieansätze ermöglicht.“ (oder belassen, wenn es einmalig ist)

### R02 – Mechanische Dreierreihen
- **Kategorie:** Satzschablone · Häufigkeit: hoch · Kontextabhängigkeit: **hoch** · **G1** (bei Häufung G2)
- **Schwäche:** Aufzählungen mit genau drei Gliedern, besonders Adjektivtriaden („präzise, schonende und effiziente“), in fast jedem Absatz; das dritte Glied ist oft redundant oder unbelegt.
- **Strategie:** prüfen, ob jedes Glied belegt und unterscheidbar ist. Unbelegte Glieder streichen, sachlich vollständige Aufzählungen belassen (z. B. „Pump-, Stokes- und akustische Welle“ sind genau drei beteiligte Wellen).
- **Beispiel:** „eine besonders präzise, schonende und effiziente Materialbearbeitung“ → „eine präzise Materialbearbeitung mit geringer thermischer Schädigung“ (wenn nur das belegt ist).

### R03 – Gleichförmige Satzlängen und wiederholte Satzanfänge
- **Kategorie:** Satzrhythmus · Häufigkeit: mittel · Kontextabhängigkeit: hoch · **G1**
- **Erkennung:** Scan-Statistik: Variationskoeffizient der Satzlänge < 0,30 bei ≥ 8 Sätzen; derselbe Satzanfang in ≥ 12 % der Sätze.
- **Strategie:** variieren **nur, wo die Informationsstruktur es nahelegt** (Thema-Rhema, siehe `sentence_structures.md`). Kurze Sätze für Kernaussagen, längere für Begründungen. Keine künstliche Variation.
- **Ausnahme:** Gleichförmige Anfänge in Aufzählungen, Definitionen oder Methodenschritten sind funktional.

### R04 – Kommentar-Anhang: „…, was die Bedeutung von X unterstreicht“ / „…, wodurch …“
- **Kategorie:** Satzschablone · Häufigkeit: hoch · Kontextabhängigkeit: mittel · **G1**
- **Schwäche:** An eine Sachaussage wird eine bewertende Deutung angehängt. Das deutsche Gegenstück zu den von Reinhart et al. 2025 gefundenen nachgestellten Partizipialkonstruktionen (*…, highlighting the importance of*).
- **Strategie:** Ist die Deutung Inhalt, einen eigenen Satz mit Begründung bilden; ist sie Floskel, streichen.
- **Ausnahme:** „…, wodurch die Duktilität steigt“ ist eine Sachfolge und wird **belassen**.

### R05 – Negativer Parallelismus / Strohmann-Kontrast: „Es geht nicht um X, sondern um Y“
- **Kategorie:** Satzschablone · Häufigkeit: mittel · Kontextabhängigkeit: mittel · **G1**
- **Schwäche:** Es wird ein Kontrast zu einer Position aufgebaut, die niemand vertreten hat.
- **Strategie:** Y direkt aussagen.
- **Ausnahme:** echte Abgrenzung von einer naheliegenden Fehlannahme (T4: „ist nicht der Modenfeldradius selbst maßgeblich, sondern die effektive Fläche“ ist **legitim**, weil beide Größen vorher eingeführt sind).

### R06 – Gedankenstrich- und Doppelpunkthäufung
- **Kategorie:** Satzschablone · Häufigkeit: mittel · Kontextabhängigkeit: hoch · **G1**
- **Erkennung:** mehr als 8 Gedankenstriche pro 1000 Wörter.
- **Strategie:** Einschübe als eigene Sätze oder Nebensätze; Doppelpunkt-„Enthüllungen“ („Das Ergebnis: …“) in Aussagesätze umwandeln.

### R07 – Rhetorische Fragen
- **Kategorie:** Satzschablone · Häufigkeit: mittel · Kontextabhängigkeit: mittel · **G2**
- **Strategie:** als Aussage oder Forschungsfrage formulieren. Mannheim rät von rhetorischen Fragen in Wissenschaftstexten ab.
- **Ausnahme:** explizit formulierte Forschungsfragen („Forschungsfrage 1: …?“).

### R08 – „Dies/Das“ am Satzanfang ohne Bezugsnomen
- **Kategorie:** Bezug · Häufigkeit: hoch · Kontextabhängigkeit: hoch · **G1**
- **Schwäche:** Bei mehreren möglichen Bezugspunkten ist unklar, worauf sich „Dies“ bezieht (Mainz: eindeutige Bezüge).
- **Strategie:** ein Bezugsnomen setzen („Dieser Zusammenhang“, „Diese Abhängigkeit“).
- **Ausnahme:** genau ein möglicher Bezug im vorangehenden Satz.

---

## 7. V – Vagheit und Hedging

### V01 – Hedging-Häufung: „könnte möglicherweise eventuell“
- **Kategorie:** Vagheit · Häufigkeit: mittel · Kontextabhängigkeit: mittel · **G2**
- **Schwäche:** doppelte Abschwächung; der Grad der Unsicherheit bleibt unklar.
- **Strategie:** genau einen Marker behalten, der dem Befund entspricht (siehe `scientific_argumentation.md`, Abschnitt Hedging). **Den Grad der Unsicherheit nicht verändern.**
- **Beispiel:** „Dies könnte möglicherweise auf Oberflächenoxidation zurückzuführen sein.“ → „Dies ist möglicherweise auf Oberflächenoxidation zurückzuführen.“

### V02 – Vage Zuschreibung: „Studien zeigen …“, „Experten sind sich einig …“, „In der Literatur wird häufig …“
- **Kategorie:** Vagheit/Beleg · Häufigkeit: hoch · Kontextabhängigkeit: gering · **G3**
- **Schwäche:** Autorität ohne Quelle (Wikipedia: *vague attributions*).
- **Strategie:** **Klasse B markieren.** Niemals selbst eine Quelle einsetzen. Steht die Quelle an anderer Stelle im Text, darauf hinweisen.
- **Beispiel:** „Studien zeigen, dass HIP die Porosität auf unter 0,01 % reduziert.“ → „Heißisostatisches Pressen (HIP) reduziert die Porosität auf unter 0,01 % ⟨B: Quelle fehlt⟩.“

### V03 – Vage Quantoren: „zahlreiche, diverse, eine Vielzahl von, unterschiedliche Aspekte“
- **Kategorie:** Vagheit · Häufigkeit: hoch · Kontextabhängigkeit: hoch · **G1**
- **Strategie:** Elemente nennen oder Menge angeben. Bei echter Unbestimmtheit belassen („zahlreiche Arbeiten [3–11]“ ist belegt und präzise genug).

### V04 – Überverallgemeinerung: „stets, immer, grundsätzlich, in allen Fällen“
- **Kategorie:** Vagheit/Fachlich · Häufigkeit: mittel · Kontextabhängigkeit: hoch · **G1**
- **Schwäche:** Der Gültigkeitsbereich fehlt; das ist oft fachlich falsch (**Klasse F**).
- **Strategie:** Ist die Aussage tatsächlich allgemeingültig (Erhaltungssatz), belassen; sonst **F markieren** und den Gültigkeitsbereich erfragen.
- **Beispiel (T1):** „Diese Verschiebung ist stets unabhängig von der Dotierung des Faserkerns.“ → markieren: ⟨F: Die Schallgeschwindigkeit $v_A$ hängt von der Kernzusammensetzung ab; damit hängt $\nu_B$ über $v_A$ von der Dotierung ab. Aussage prüfen.⟩

### V05 – Füllwörter und Abtönungspartikeln: „eigentlich, gewissermaßen, im Grunde, quasi, eben, ja, wohl, durchaus“
- **Kategorie:** Füllwort · Häufigkeit: mittel (häufiger bei Menschen) · Kontextabhängigkeit: mittel · **G1**
- **Strategie:** streichen (Mainz-Liste: aber, auch, bloß, denn, eben, eigentlich, etwa, halt, ja, nämlich, vielleicht, wohl). „etwa“ als Näherungsangabe („etwa 10 ns“) und „wohl“ als bewusstes Hedging sind **keine** Füllwörter.

---

## 8. A – Argumentationsschablonen (nicht per Regex erkennbar)

### A01 – Scheinkausalität
Ein kausaler Konnektor („da“, „weil“, „daher“) verbindet Aussagen ohne Ursache-Wirkung-Beziehung oder mit falscher Richtung. **Klasse L.** Strategie: die Relation korrekt benennen (temporal, additiv) oder die fehlende Prämisse markieren.

### A02 – Zirkuläre Erklärung
Die Erklärung wiederholt die Definition („Die Schwelle ist erreicht, wenn die Leistung den Schwellwert überschreitet“). **Klasse L.** Strategie: das Kriterium nennen (Smith-Kriterium) oder markieren.

### A03 – Redundanz zwischen Absätzen
Derselbe Gedanke steht in zwei Absätzen mit anderen Worten. Der Scan meldet Satzpaare mit hoher Überschneidung. **Klasse S.** Strategie: die präzisere Fassung behalten und die zweite streichen oder zum Querverweis machen.

### A04 – Symmetrisches Pro und Contra ohne Gewichtung
„Einerseits … andererseits …“ ohne Schluss. Strategie: Gewichtung nach Datenlage ergänzen, **sofern im Text belegt**, sonst den Autor fragen.

### A05 – „Herausforderungen und Potenzial“-Schema
„Trotz dieser Herausforderungen bietet X großes Potenzial für …“ ist ein schematischer Abschluss (Wikipedia: *challenges and future prospects*). Strategie: konkrete Grenze und konkrete Anwendung nennen oder streichen.

### A06 – Absatzschablone: Themensatz – drei Punkte – Resümee
Jeder Absatz hat dieselbe Form. Strategie: die Absatzform nach Funktion wählen (Definition, Herleitung, Vergleich, Einschränkung; siehe `scientific_argumentation.md`). Nicht jeder Absatz braucht einen Themensatz oder ein Resümee.

---

## 9. Kurzübersicht: Prüffragen vor jeder Änderung
1. Welche Information trägt die Formulierung? Wenn keine: streichen.
2. Welche logische Relation stellt sie her? Stimmt die Relation?
3. Ist sie in diesem Fach und Textteil konventionell?
4. Kommt sie gehäuft vor (mehr als einmal pro Absatz bzw. Seite)?
5. Verändert meine Alternative Modalität, Gültigkeitsbereich, Richtung oder Gewichtung der Aussage? Wenn ja: nicht ändern, sondern markieren.
6. Ist meine Alternative wirklich besser oder nur anders? Wenn nur anders: belassen.
