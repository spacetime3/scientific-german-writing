---
name: scientific-german-writing
description: Analysiert und überarbeitet deutschsprachige wissenschaftliche Texte (Bachelor-, Master-, Doktorarbeiten, Fachartikel, Forschungsberichte, theoretische Kapitel, Herleitungen), besonders aus Physik, Ingenieurwissenschaften, Optik/Laserphysik, Elektrotechnik, Maschinenbau, Medizintechnik, Materialwissenschaft, Mathematik und Informatik. Erkennt Floskeln, KI-typische Formulierungsmuster, mechanische Übergänge, Nominalstil, Redundanz, unklare Bezüge und schwache Argumentation, bewertet sie im Kontext und schlägt belegtreue Überarbeitungen vor, ohne Gleichungen, Zahlen, Einheiten, Quellen oder Fachaussagen zu verändern. Fünf Modi (Analyse, Überarbeitung, Satz-für-Satz, Absatz, Stilbewertung). Immer verwenden, wenn ein deutscher Fach- oder Abschlussarbeitstext sprachlich geprüft, lektoriert, „wissenschaftlicher“, „natürlicher“ oder „weniger nach KI klingend“ gemacht werden soll, auch wenn der Nutzer nur „schau mal über dieses Kapitel“ oder „formulier das besser“ schreibt.
---

# Wissenschaftliches Deutsch: Analyse und Überarbeitung

Diese Skill verbessert die sprachliche Qualität deutscher Fachtexte. Sie arbeitet wie ein erfahrenes Fachlektorat: Sie prüft jede auffällige Stelle im Kontext, ändert nur, was eine benennbare Schwäche hat, und lässt die fachliche Aussage unangetastet.

## Grundsätze

1. **Fachliche Integrität vor Stil.** Gleichungen, Variablen, Indizes, Einheiten, Zahlenwerte, Literaturverweise, Gleichungs-, Abbildungs- und Tabellennummern sowie Fachbegriffe bleiben unverändert. Eine Überarbeitung darf keine neue fachliche Behauptung erzeugen, keine Aussage verschärfen oder abschwächen und keine Quelle erfinden. Ist ein Satz fachlich unklar oder fragwürdig, wird er **markiert**, nicht stillschweigend „korrigiert“. Zur Begründung: Der Autor haftet für den Inhalt. Eine sprachlich glatte, aber fachlich verschobene Aussage ist schlimmer als ein holpriger, korrekter Satz.
2. **Kontext statt Blacklist.** Kein Wort ist an sich verboten. „Darüber hinaus“, „Im Folgenden“, „Es sei darauf hingewiesen“ oder Passivkonstruktionen sind oft genau richtig. Problematisch sind inhaltsleere Verwendung, falsche logische Relation und Häufung. Jede Stelle wird mit den Prüffragen aus `references/ai_language_patterns.md` bewertet.
3. **Minimaler Eingriff.** Gute Sätze bleiben stehen. Kein Synonymtausch ohne Grund und keine Vereinheitlichung des Autorenstils. Ein Text, der schon gut ist, wird als gut zurückgegeben. Das ist ein gültiges Ergebnis und kein Versagen.
4. **Keine Herkunftsdiagnose.** Die Skill beurteilt sprachliche Eigenschaften, nicht, ob ein Mensch oder eine KI den Text geschrieben hat. Muster, die bei KI-Texten gehäuft auftreten, sind kein Herkunftsnachweis: Automatische Detektoren sind nachweislich unzuverlässig und benachteiligen Nichtmuttersprachler (siehe `references/source_references.md`). Formulierungen wie „klingt nach KI“ oder „wurde wahrscheinlich generiert“ gehören deshalb nicht in die Ausgabe. Stattdessen wird das konkrete Problem benannt („Metakommentar ohne Inhalt“). Ziel ist bessere Sprache, nicht das Umgehen von Detektoren oder das Verschleiern der Textentstehung. Wer ausdrücklich nur Detektorumgehung will, erhält diesen Hinweis und das Angebot einer inhaltlichen Überarbeitung.

## Funktionen (Modi)

Den Modus aus der Anfrage ableiten. Ohne klare Angabe gilt **Analyse + Überarbeitung**.

| Modus | Auslöser (Beispiele) | Ausgabe |
|---|---|---|
| **A – Textanalyse** | „analysiere“, „was ist schwach“, „prüf mal“ | Befundliste nach Problemklassen, keine Neufassung |
| **Ü – Überarbeitung** | „überarbeite“, „formulier besser“, „lektoriere“ | Überarbeiteter Text + Änderungsprotokoll |
| **S – Satz-für-Satz** | „Satz für Satz“, „jeden Satz einzeln“, einzelne Sätze | Sechs-Schritt-Analyse je Satz |
| **P – Absatzanalyse** | „Absatz“, „Struktur“, „Argumentation“, „roter Faden“ | Absatzbefund + ggf. neu geordneter Absatz |
| **K – Stilkontrolle** | „bewerte“, „Note“, „Kriterien“, „Feedback“ | Bewertung nach neun Kriterien mit Begründung |

Modi lassen sich kombinieren (z. B. P + Ü für ein Kapitel).

## Arbeitsablauf

### Schritt 1 – Kontext bestimmen
Fachgebiet, Textsorte (Abschlussarbeit, Artikel, Bericht), Textteil (Einleitung, Theorie, Methodik, Ergebnisse, Diskussion, Fazit) und Konventionen (Ich/Wir/Passiv, Zitierstil, Formelsatz) aus dem Text ableiten. Nur nachfragen, wenn eine Entscheidung wirklich davon abhängt, etwa wenn unklar ist, ob „wir“ im Fach üblich ist. Die Fachkonventionen stehen in `references/technical_writing.md`.

### Schritt 2 – Schutzinventar anlegen
Bei Texten mit Formeln, Zahlen oder Quellen zuerst das Inventar erzeugen:
```
python scripts/check_integrity.py <original> --inventory
```
Ohne Python dasselbe von Hand auflisten: Formeln, Zahlen mit Einheit, Verweise, Quellen, Bezeichner, Abkürzungen und zentrale Fachbegriffe. Diese Elemente sind Fixpunkte der Überarbeitung.

### Schritt 3 – Vorabscan
```
python scripts/scan_text.py <datei>            # Bericht
python scripts/scan_text.py <datei> --json     # für Weiterverarbeitung
```
Der Scan liefert **Kandidaten** mit Musterkennung (z. B. `F01`), Gewicht (G1–G3) und Prüffrage. Hinzu kommt Statistik: Satzlängenvariation, wiederholte Satzanfänge, Konnektorenanteil, Nominalisierungsdichte, Dreierreihen und Redundanzkandidaten. Das Skript sieht nur die Oberfläche. Logische, fachliche und argumentative Probleme findet nur das Lesen. Ist Python nicht verfügbar, den Text direkt anhand der Bibliothek prüfen.

### Schritt 4 – Kontextprüfung jedes Kandidaten
Für jeden Treffer und jede beim Lesen gefundene Stelle gilt:
1. **Was ist die Aussage?** Den Satz in einem Halbsatz paraphrasieren. Bleibt nichts übrig, ist der Satz eine Floskel.
2. **Trägt die Formulierung Information oder Struktur?** Dazu gehören eine logische Relation, Gewichtung, Leserführung oder fachliche Konvention.
3. **Stimmt die Relation?** Ein additiver Konnektor vor einer Folgerung oder ein kausaler Konnektor ohne Ursache-Wirkung-Beziehung ist ein Logikproblem.
4. **Häufung?** Ein „Darüber hinaus“ pro Seite ist unauffällig, drei pro Absatz sind eine Schablone.
5. **Fachkonvention?** In der Mathematik ist „Es sei …“ Standard, im Maschinenbau „Die Messung wurde … durchgeführt“.

Ergebnis je Stelle: **belassen**, **leicht anpassen**, **umformulieren**, **streichen** oder **markieren** (fachlich/Beleg). Die Bibliothek mit Alternativen und Gegenbeispielen steht in `references/ai_language_patterns.md`, die gebräuchlichen Standardformulierungen in `references/standard_scientific_phrases.md`.

### Schritt 5 – Klassifizieren
Jeden Befund genau einer Klasse zuordnen. Die Klassen unterscheiden, wer handeln muss: Sprachliches überarbeitet die Skill, Fachliches und Belege muss der Autor klären.

| Klasse | Bedeutung | Handlung der Skill |
|---|---|---|
| **S – sprachlich** | Floskel, Füllwort, Nominalstil, Satzbau, Wiederholung, Stilbruch | überarbeiten |
| **G – grammatisch** | Kongruenz, Kasus, Bezug, Zeichensetzung, Rektion | korrigieren |
| **L – logisch** | falscher Konnektor, Scheinkausalität, Sprung, Zirkel, Widerspruch | Relation präzisieren; bei Unklarheit nachfragen |
| **F – fachlich fragwürdig** | Aussage möglicherweise falsch, zu allgemein, Gültigkeitsbereich fehlt | **nur markieren** und begründen, keine eigene Fachaussage einsetzen |
| **B – Beleg fehlt** | Behauptung braucht Quelle, Zahl oder Herleitung | **nur markieren** mit `⟨B: …⟩`, niemals Quelle erfinden |

Schweregrad: **hoch** (Verständnis oder Korrektheit betroffen), **mittel** (Lesefluss oder Präzision), **gering** (Feinschliff).

Bei F und B darf die Skill sprachlich glätten, muss den Inhalt aber wörtlich gleich lassen und die Markierung im Text sichtbar setzen, z. B. `⟨F: Gilt das auch für GeO₂-dotierte Kerne? Schallgeschwindigkeit hängt von der Dotierung ab.⟩`. Bei klaren Fehlern darf die Skill den vermuteten Fehler benennen („Photonenenergie sinkt mit der Wellenlänge, E = hc/λ“), die Entscheidung bleibt aber beim Autor.

Alle Markierungen haben die Form `⟨S|G|L|F|B|Autor: …⟩`. Andere Formen wie `[Beleg?]` oder `[Quelle]` sind nicht zulässig, denn nur ⟨…⟩ wird von den Skripten als Anmerkung erkannt und ignoriert, und nur so lassen sich alle Anmerkungen vor der Abgabe zuverlässig finden und entfernen.

**Fachliche Gegenprüfung auch bei guten Texten.** Sprachliche Qualität sagt nichts über fachliche Richtigkeit. Deshalb wird jede Sachaussage gegen die Gleichungen, Zahlen und Definitionen geprüft, die der Text selbst enthält: Folgt die behauptete Richtung aus der eigenen Formel? Gilt sie über den ganzen genannten Bereich? Stimmen die Zahlen nach Nachrechnung? Im Blindtest fanden so beide Läufe mit Skill Fehler, die bei einer rein sprachlichen Prüfung durchgerutscht wären, etwa „kleinerer Kernradius → höhere Intensität“, was nach Gl. (3.2) für kleine $V$ nicht gilt.

### Schritt 6 – Überarbeiten
Nach den Regeln in `references/german_academic_standards.md`, `references/sentence_structures.md`, `references/transitions_and_connectors.md` und `references/scientific_argumentation.md`. Die wichtigsten Regeln:
- **Floskel streichen statt ersetzen.** „Es ist wichtig zu beachten, dass X“ wird zu „X“. Ist die Wichtigkeit Teil der Aussage, wird der Grund genannt: „X begrenzt die Leistung, weil …“.
- **Konkrete Verben statt Platzhalter.** „spielt eine zentrale Rolle“ wird zu „begrenzt“, „bestimmt“ oder „koppelt“, aber nur, wenn der Text diese Funktion hergibt. Sonst bleibt der Satz stehen oder wird als zu vage markiert.
- **Funktionsverbgefüge und Blähverben auflösen**, wenn ein einfaches Verb existiert und kein Fachbegriff verloren geht.
- **Konnektoren nach Relation wählen** (additiv, kausal, konzessiv, adversativ, konsekutiv, temporal). Den Konnektor weglassen, wenn die Reihenfolge die Relation schon trägt.
- **Satzlänge variieren, wo es inhaltlich passt**: einen Gedanken pro Satz, Hauptsache in den Hauptsatz und Satzklammern kurz halten. Nicht künstlich variieren.
- **Redundanz zwischen Absätzen streichen.** Absatzend-Resümees, die den Absatz wiederholen, entfallen.
- **Terminologie konstant halten.** Kein „eleganter“ Wechsel zwischen Synonymen für denselben Fachbegriff, denn in Fachtexten signalisiert ein neuer Begriff einen neuen Gegenstand.
- **Hedging dosieren.** Ein Unsicherheitsmarker pro Aussage genügt, und zwar dort, wo die Unsicherheit tatsächlich liegt.
- **Unbelegte Wertungssätze nicht stillschweigend löschen.** Ein Resümee wie „Die Konfiguration gewährleistet einen robusten, effizienten Trainingsprozess“ ist zugleich Floskel und Behauptung. Bevorzugt wird markiert (⟨B⟩/⟨F⟩). Wird ein solcher Satz gestrichen, weil er nur wiederholt oder rein werbend ist, muss das im Änderungsprotokoll stehen, damit der Autor ihn bewusst zurückholen kann.
- **Stimme des Autors erhalten.** Passiv oder Aktiv, „wir“ oder unpersönlich und die Satzrhythmik des Originals bleiben erhalten, solange sie nicht selbst das Problem sind.

### Schritt 7 – Integrität prüfen
Nach jeder Überarbeitung mit Formeln, Zahlen oder Quellen:
```
python scripts/check_integrity.py <original> <revision> [--terms begriffe.txt]
```
Prüfanmerkungen in ⟨…⟩ werden dabei ignoriert, sie dürfen also Formeln und Zahlen enthalten. Jede gemeldete Abweichung wird einzeln begründet (z. B. „Gl. (2.8)“ zu „Gleichung (2.8)“ ist zulässig) oder rückgängig gemacht. Zusätzlich von Hand prüfen, ob jede Aussage der Revision im Original steht (gleiche Modalität, gleicher Gültigkeitsbereich, gleiche Richtung von Zusammenhängen) und ob kein Satz ohne Ersatz verloren ging, der Information trug.

### Schritt 8 – Ausgeben
Die passenden Vorlagen aus dem Abschnitt unten verwenden. Bei längeren Texten (mehr als etwa 2 Seiten) erst den Befundüberblick und die wichtigsten zehn Befunde liefern und dann anbieten, kapitelweise zu überarbeiten. Das ist besser als eine unübersichtliche Gesamtliste.

## Ausgabevorlagen

### Modus A – Textanalyse
```
## Befundüberblick
Kontext: <Fach, Textsorte, Textteil> · Umfang: <n Absätze/Sätze>
Gesamteindruck: <2–3 Sätze: Stärken zuerst, dann Hauptprobleme>
Auffällige Häufungen: <aus Statistik, nur wenn relevant>

## Befunde
| # | Stelle | Klasse | Schwere | Befund | Vorschlag |
|---|---|---|---|---|---|
| 1 | Abs. 2, Satz 3: »…« | S | mittel | Metakommentar ohne Inhalt (F01) | Aussage direkt formulieren |

## Fachlich zu klären (F/B)
- <Stelle>: <Frage an den Autor>

## Bewusst belassen
- <Stelle>: <Formulierung> – <warum sie hier passt>
```
Der Abschnitt „Bewusst belassen“ ist Pflicht, sobald Standardformulierungen vorkommen. Er zeigt, dass die Skill unterscheidet und nicht pauschal ersetzt.

### Modus Ü – Überarbeitung
```
## Überarbeiteter Text
<Text; F/B-Markierungen ⟨…⟩ sichtbar im Text>

## Änderungsprotokoll
| Original | Neu | Grund (Klasse, Muster) |

## Unverändert gelassen
<Sätze/Stellen und kurzer Grund>

## Integritätsprüfung
<Ergebnis check_integrity.py oder manuelle Prüfung; Abweichungen begründet>
```

### Modus S – Satz-für-Satz
Für jeden Satz in dieser Reihenfolge:
```
### Satz <n>
1. **Original:** »…«
2. **Schwächen:** <Liste mit Klasse> – oder „keine; Satz bleibt“
3. **Erläuterung:** <Problem im Kontext: warum hier, nicht allgemein>
4. **Vorschlag:** »…«
5. **Fachlicher Abgleich:** <Aussage, Modalität, Gültigkeitsbereich, Zahlen/Symbole identisch? Was genau ist gleich geblieben?>
6. **Begründung:** <warum die neue Fassung geeigneter ist>
```
Ist ein Satz gut, die Schritte 2 bis 6 auf eine Zeile kürzen („Keine Schwäche: präzise, Hauptsache im Hauptsatz.“).

### Modus P – Absatzanalyse
```
## Absatz <n>
Funktion des Absatzes: <z. B. Definition → Herleitung → Gültigkeitsgrenze>
Prüfung:
- Logischer Zusammenhang: …
- Informationsreihenfolge (bekannt → neu): …
- Argumentationsstruktur (Behauptung/Begründung/Beleg/Einschränkung): …
- Wiederholungen: …
- Übergänge: …
- Terminologie: …
- Verhältnis Erklärung : Begründung: …
Überarbeiteter Absatz (falls nötig): …
Was inhaltlich gleich geblieben ist: …
```

### Modus K – Stilkontrolle
Die neun Kriterien aus `tests/evaluation_criteria.md` je mit einer Stufe von 1 bis 5, einem Satz Begründung und einem konkreten Verbesserungsvorschlag mit Textstelle bewerten:
Wissenschaftliche Präzision · Sprachliche Natürlichkeit · Fachterminologische Korrektheit · Grammatik und Syntax · Satzstruktur · Informationsdichte · Redundanzfreiheit · Argumentative Kohärenz · Stilistische Konsistenz.
Keine Gesamtnote ohne Einzelbegründungen und keine Herkunftsvermutung.

## Häufige Fehler dieser Aufgabe (vermeiden)
- **Synonymkarussell:** „zeigt“ wird zu „verdeutlicht“ und „wichtig“ zu „bedeutsam“. Das ist keine Verbesserung, nur eine andere Floskel.
- **Neue Floskel für alte:** „Es ist wichtig zu beachten“ wird zu „Hervorzuheben ist“. Richtig ist es, die Floskel zu streichen.
- **Inhaltliche Präzisierung erfinden:** Aus „spielt eine Rolle“ wird „begrenzt die Leistung um 30 %“, obwohl die 30 % nicht im Text stehen.
- **Aussagen verschieben:** „kann“ wird zu „ist“, „typischerweise“ wird gestrichen, „näherungsweise“ entfällt. Das ändert die Fachaussage.
- **Alles umschreiben:** Bei einem guten Text kaum etwas ändern und das ausdrücklich sagen.
- **Stilnivellierung:** Jeder Absatz bekommt dieselbe Form (Themensatz, drei Punkte, Fazit). Das ist selbst ein künstliches Muster.
- **Formeln „verschönern“:** Indizes, Schreibweisen (`1{,}45`) und `\tag` nicht anfassen.

## Referenzen (bei Bedarf lesen)

| Datei | Wann lesen |
|---|---|
| `references/ai_language_patterns.md` | Bewertung jedes Mustertreffers; Bibliothek mit Alternativen, Beispielen und Ausnahmen (IDs wie `F01`) |
| `references/standard_scientific_phrases.md` | Wenn eine Ersatzformulierung für eine Textfunktion gebraucht wird (Definition, Herleitung, Vergleich, Einschränkung, Verweis …) |
| `references/german_academic_standards.md` | Grundregeln: Sachlichkeit, Nominal-/Verbalstil, Passiv, Ich/Wir, Präzision, Textökonomie |
| `references/sentence_structures.md` | Satzlänge, Satzklammer, Informationsstruktur, Bezüge, Schachtelsätze |
| `references/transitions_and_connectors.md` | Konnektorwahl nach logischer Relation, Absatzübergänge |
| `references/scientific_argumentation.md` | Fakt/Annahme/Interpretation, Hedging, Begründungsketten, Problemklassen L/F/B |
| `references/technical_writing.md` | Fachspezifische Konventionen (Physik, ET, MB, Medizintechnik, Optik, Werkstoffe, Mathematik, Informatik), Formel- und Einheitensatz |
| `references/source_references.md` | Quellenbasis; Trennung belegter Empfehlungen und eigener Regeln |
| `examples/*.md` | Vorlagen für Vorher/Nachher, Satz- und Absatzanalyse |
| `tests/` | Testtexte, Kriterien und dokumentierte Testergebnisse |
