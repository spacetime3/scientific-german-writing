# Wissenschaftliche Argumentation, epistemischer Status und Problemklassen

## 1. Epistemischer Status jeder Aussage
Jede Aussage eines Fachtextes gehört zu einer dieser Kategorien. Die Sprache muss sie erkennbar machen, und **eine Überarbeitung darf den Status nicht ändern**.

| Status | Sprachliche Kennzeichen | Beispiel |
|---|---|---|
| Messung/Beobachtung | Präteritum/Perfekt, Zahl + Einheit, „gemessen“, „beobachtet“ | „Bei 8 l/min wurde 0,11 K/W gemessen.“ |
| Herleitung/Beweis | „folgt“, „gilt“, „ergibt sich“, Präsens | „Aus Gl. (2.10) folgt …“ |
| Literatur | Verweis, „nach [n]“, „berichten“, Konjunktiv I in Paraphrasen | „Lee et al. (2022) berichten, dass …“ |
| Annahme/Modell | „angenommen“, „unter der Annahme“, „in Näherung“ | „Unter der Annahme langsam veränderlicher Amplituden …“ |
| Interpretation | „deutet darauf hin“, „lässt sich erklären durch“, „vermutlich“ | „Die Abweichung ist vermutlich auf … zurückzuführen.“ |
| Spekulation/Ausblick | „denkbar“, „könnte“, „bleibt zu prüfen“ | „Ob dies auch für … gilt, bleibt zu prüfen.“ |

**Typische Statusverschiebungen durch Überarbeitung (verboten):**
- Hedging streichen: „deutet darauf hin, dass X“ → „X“ (Interpretation wird zur Tatsache)
- Modalverb tauschen: „kann zu … führen“ → „führt zu …“
- Näherung tilgen: „näherungsweise“, „typischerweise“, „in guter Näherung“ entfernen
- Gültigkeitsbereich tilgen: „im Nennbetrieb“ entfernen
- Quelle verschieben: Durch Satzteilung steht der Verweis nicht mehr bei der belegten Teilaussage.
- Richtung verschieben: „beeinflusst“ → „verringert“ (Richtung nicht im Original)
- Generalisieren: „in Standard-Singlemode-Fasern“ → „in Glasfasern“

## 2. Hedging (Vorsichtsformulierungen)
- [Q Hyland 1998, vgl. `source_references.md`] Hedging ist ein legitimes und notwendiges Mittel, um den Grad der Gewissheit einer Aussage zu signalisieren. Es ist kein Stilfehler.
- [R] Problematisch sind (a) **Häufung** mehrerer Marker in einer Aussage (V01), (b) **pauschales Hedging** aller Aussagen, auch gesicherter, und (c) **fehlendes Hedging** bei Interpretationen.
- [R] Strategie: Unsicherheit dort markieren, wo sie liegt, mit genau einem Marker. Bei (b) und (c) **nicht selbst entscheiden**, sondern als F markieren: „⟨F: Ist das gemessen oder vermutet?⟩“.

## 3. Argumentationsstrukturen im Absatz
Ein Absatz hat eine Funktion. Gängige Muster in Natur- und Ingenieurwissenschaften:
1. **Definition → Eigenschaft → Konsequenz** (Theorie)
2. **Behauptung → Begründung → Beleg → Einschränkung** (Diskussion)
3. **Ausgangsgleichung → Annahme → Umformung → Ergebnis → Gültigkeitsbereich** (Herleitung)
4. **Ziel → Vorgehen → Parameter → Ergebnis** (Methodik)
5. **Befund → Vergleich mit Literatur → Erklärung → offene Frage** (Diskussion)

**Prüffragen für die Absatzanalyse (Modus P):**
- Welche Funktion hat der Absatz? Erfüllt jeder Satz eine Rolle darin?
- Ist die Reihenfolge logisch? Kommt die Begründung vor oder nach der Behauptung, und ist das gewollt?
- Gibt es Sprünge (fehlende Zwischenschritte) oder Zirkel?
- Verhältnis von Erklärung und Begründung: Wird nur beschrieben, was passiert, oder auch, warum? Fachtexte brauchen beides. Ein Absatz aus reinen Wertungen („wichtig“, „entscheidend“) ohne Begründung ist schwach.
- Wird eine Einschränkung genannt, wo das Modell an Grenzen stößt?
- Endet der Absatz mit einem Resümee, das nur wiederholt? Dann streichen.

## 4. Problemklassen L, F, B im Detail
### L – logisches Problem
Erkennungszeichen: Konnektor passt nicht zur Relation; Folgerung ohne Prämisse; Widerspruch zu einer früheren Aussage; Zirkelschluss; Kausalbehauptung aus Korrelation.
Handlung: Relation präzisieren, **wenn der Text die richtige Relation eindeutig hergibt**; sonst markieren: ⟨L: Folgt X aus Y? Es fehlt der Schritt …⟩.

### F – fachlich fragwürdig
Erkennungszeichen: Widerspruch zu Lehrbuchwissen; Allaussage ohne Gültigkeitsbereich; Größen verwechselt (Faserlänge vs. effektive Länge, Leistung vs. Intensität); Einheit oder Größenordnung unplausibel; Gleichung und Text widersprechen sich.
Handlung: **markieren und begründen**, mit kurzer Fachbegründung oder Prüfrechnung („2·1,45·5960 m/s / 1550 nm ≈ 11,2 GHz, passt zu 11,1 GHz“). Die Skill formuliert keine eigene Ersatzaussage in den Fließtext, darf aber im Kommentar eine wahrscheinliche Korrektur nennen.
Beispiel: „Da die Photonenenergie mit zunehmender Wellenlänge steigt, …“ → ⟨F: $E = hc/\lambda$, die Photonenenergie **sinkt** mit der Wellenlänge. Die Begründung für die Eignung infraroter Laser ist eher die Wasserabsorption (siehe nächsten Absatz). Bitte prüfen.⟩

### B – Beleg fehlt
Erkennungszeichen: vage Zuschreibung (V02); konkrete Zahl ohne Quelle oder Messung; Behauptung über den Forschungsstand ohne Verweis; „bekanntlich“ bei nicht trivialem Wissen.
Handlung: ⟨B: Quelle fehlt⟩ setzen. **Niemals** eine Quelle, Autorin, Jahreszahl, DOI oder Zahl erfinden, auch nicht als „Beispiel“. Steht eine passende Quelle an anderer Stelle im selben Text, darf die Skill darauf hinweisen („[6] aus Abs. 3 passt eventuell?“), setzt sie aber nicht selbst ein.

## 5. Erklärung vs. Begründung
- **Erklärung:** Wie funktioniert etwas? (Mechanismus)
- **Begründung:** Warum ist eine Aussage oder Entscheidung gerechtfertigt? (Argument, Beleg)
- [R] KI-typisch und auch bei unerfahrenen Schreibenden häufig sind Absätze, die Bedeutung **behaupten** (Wertung) statt zu erklären oder zu begründen. Die Überarbeitung ersetzt die Wertung durch die im Text vorhandene Erklärung oder streicht sie. Sie erfindet keine Begründung.

## 6. Redundanz und Wiederholung
- [R] Wiederholung ist legitim als Zusammenfassung am Kapitelende, als Wiederaufnahme zur Kohäsion (gleicher Fachbegriff) und als Erinnerung vor einer Folgerung nach langer Herleitung.
- [R] Redundant ist dieselbe Aussage in zwei Absätzen ohne neue Funktion, ein Absatzend-Resümee direkt nach dem Inhalt und die Einleitung eines Abschnitts, die den Titel paraphrasiert.
