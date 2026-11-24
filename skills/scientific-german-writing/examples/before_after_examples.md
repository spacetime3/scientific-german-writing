# Vorher/Nachher-Beispiele

Jedes Beispiel nennt das Muster aus `references/ai_language_patterns.md`, die Problemklasse und **was fachlich gleich bleibt**. Drei Beispiele zeigen ausdrücklich, wann **nicht** geändert wird.

---

### 1. Floskel streichen statt ersetzen (F01, S)
**Vorher:** Es ist wichtig zu beachten, dass die Wahl der Wellenlänge, die Pulsdauer und die Pulsenergie entscheidende Faktoren für den Behandlungserfolg sind.
**Nachher:** Der Behandlungserfolg hängt wesentlich von Wellenlänge, Pulsdauer und Pulsenergie ab.
**Warum:** Der Metakommentar trägt keine Information. Die Aufzählung wird parallel (drei Größen statt Nominalisierung + zwei Größen). „Entscheidend“ bleibt als „wesentlich“ erhalten, die Stärke der Aussage also auch.
**Gleich geblieben:** dieselben drei Parameter, dieselbe Abhängigkeitsrichtung.
**Falsch wäre:** „Hervorzuheben ist, dass …“ (neue Floskel) oder „Der Behandlungserfolg hängt von … ab“ (Abschwächung: „entscheidend“ ginge verloren).

### 2. Platzhalter „Rolle“ durch Funktion ersetzen (E02, S)
**Vorher:** Die stimulierte Brillouin-Streuung (SBS) spielt eine zentrale Rolle bei der Leistungsskalierung schmalbandiger Faserlaser.
**Nachher:** Die stimulierte Brillouin-Streuung (SBS) begrenzt die Leistungsskalierung schmalbandiger Faserlaser.
**Warum:** Der Abschnitt behandelt die SBS-Schwelle als Leistungsgrenze, die Funktion „begrenzt“ steht also im Text.
**Gleich geblieben:** Gegenstand, Anwendungsbereich (schmalbandig).
**Bedingung:** Geht aus dem Kontext keine Funktion hervor, bleibt der Satz stehen.

### 3. Blähnomen + Blähverb (N08, N03, S)
**Vorher:** Die Durchführung einer Abschätzung der Schwellleistung erfolgt üblicherweise mit dem Kriterium nach Smith [14].
**Nachher:** Die Schwellleistung wird üblicherweise mit dem Kriterium nach Smith [14] abgeschätzt.
**Gleich geblieben:** „üblicherweise“ (Modalität), Verweis [14] am selben Teilsatz.

### 4. Funktionsverbgefüge und Nominalkette in der Elektrotechnik (N01, N02, S)
**Vorher:** Die Ermittlung der Verlustleistung der Halbleiterschalter findet dabei unter Berücksichtigung der Schalt- und Durchlassverluste statt, wobei die Bestimmung der Schaltverluste anhand der Datenblattangaben des Herstellers zur Anwendung kommt.
**Nachher:** Die Verlustleistung der Halbleiterschalter setzt sich aus Schalt- und Durchlassverlusten zusammen; die Schaltverluste werden aus den Datenblattangaben des Herstellers bestimmt.
**Bedeutungsprüfung:** „unter Berücksichtigung von A und B“ heißt hier, dass beide Verlustarten einbezogen werden. „setzt sich aus A und B zusammen“ ist gleichwertig, weil weitere Verlustanteile im Original nicht genannt sind. Wäre das unsicher, bliebe die Formulierung „wird unter Berücksichtigung … ermittelt“ stehen.

### 5. Mechanischer Übergang → inhaltlicher Anschluss (U01 + F03, S)
**Vorher:** Darüber hinaus ist die Bandbreite des Brillouin-Gewinnspektrums von besonderer Bedeutung.
**Nachher:** Neben der Frequenzverschiebung charakterisiert die Bandbreite das Brillouin-Gewinnspektrum.
**Warum:** „von besonderer Bedeutung“ sagt nicht, wofür. Der neue Satz knüpft an den vorigen Absatz an (Thema-Rhema) und nennt die Funktion der Größe.

### 6. NICHT ändern: legitimer additiver Konnektor (U01)
**Text:** Darüber hinaus weisen L-PBF-Bauteile prozessbedingt Porosität auf.
**Entscheidung:** belassen. Der vorige Absatz behandelt das Gefüge, dieser einen zweiten, gleichrangigen Werkstoffaspekt. Es ist das einzige „Darüber hinaus“ im Text, die Relation ist also korrekt additiv.

### 7. NICHT ändern: legitimer Kontrast (R05) und Wertadjektiv (N06)
**Text:** Für nichtlineare Effekte ist nicht der Modenfeldradius selbst maßgeblich, sondern die effektive Fläche $A_{\mathrm{eff}}$, über die sich die optische Leistung verteilt.
**Entscheidung:** belassen. Beide Größen sind eingeführt, der Kontrast korrigiert eine naheliegende Fehlannahme, und „maßgeblich“ ist präzise.

### 8. NICHT ändern: mathematische Konvention (F04)
**Text:** Es sei $f$ stetig auf $[a,b]$ und differenzierbar auf $(a,b)$. Dann gibt es ein $\xi \in (a,b)$ mit …
**Entscheidung:** belassen. „Es sei“ ist eine Setzung, keine Floskel.

### 9. Unbelegte Zuschreibung markieren, nicht belegen (V02, B)
**Vorher:** Studien zeigen, dass heißisostatisches Pressen (HIP) die Porosität auf unter 0,01 % reduziert.
**Nachher:** Heißisostatisches Pressen (HIP) reduziert die Porosität auf unter 0,01 %. ⟨B: Im Original „Studien zeigen“ ohne Quelle, bitte belegen.⟩
**Falsch wäre:** eine Quelle einzusetzen, etwa „[7]“ oder „(Müller et al., 2020)“. Auch das Streichen der Zahl wäre falsch, denn sie gehört zur Aussage des Autors.

### 10. Fachlich falsche Begründung markieren (F)
**Vorher:** Da die Photonenenergie mit zunehmender Wellenlänge steigt, eignen sich infrarote Laser besonders gut für die Ablation harter Gewebe.
**Nachher:** (Satz unverändert) ⟨F: Nach $E = hc/\lambda$ sinkt die Photonenenergie mit zunehmender Wellenlänge. Vermutlich ist die Wasserabsorption gemeint. Bitte prüfen.⟩
**Warum unverändert:** Eine sprachliche Glättung würde den Fehler nur flüssiger machen. Den Satz eigenmächtig umzudrehen hieße, eine neue fachliche Aussage zu erzeugen.

### 11. Allaussage ohne Gültigkeitsbereich (V04, F)
**Vorher:** Diese Verschiebung ist stets unabhängig von der Dotierung des Faserkerns.
**Nachher:** (unverändert) ⟨F: Laut der Formel davor hängt $\nu_B$ von $v_A$ ab, und $v_A$ hängt von der Kernzusammensetzung ab. „stets unabhängig“ prüfen.⟩

### 12. Kommentar-Anhang auflösen, ohne Fachaussage zu verschieben (S04/R04, S + F)
**Vorher:** Gleichung (2.8) verdeutlicht, dass die Schwelle mit zunehmender Faserlänge sinkt, was die Bedeutung kurzer Fasern für Hochleistungsanwendungen unterstreicht.
**Nachher:** Nach Gleichung (2.8) sinkt die Schwelle mit zunehmender Faserlänge; für Hochleistungsanwendungen sind daher kurze Fasern günstig. ⟨F: Gl. (2.8) enthält $L_{\mathrm{eff}}$, nicht die Faserlänge.⟩
**Gleich geblieben:** Die Folgerung „kurze Fasern“ ist im Original enthalten („Bedeutung kurzer Fasern“), sie wird nur ausgesprochen statt behauptet. Die Größenverwechslung wird markiert, nicht korrigiert.

### 13. Zeitgeist-Einstieg mit Bedeutungsbehauptung (E01 + E02 → B)
**Vorher:** In der heutigen schnelllebigen Welt spielen Lasertechnologien eine immer größere Rolle in der Medizintechnik.
**Nachher:** Lasertechnologien werden in der Medizintechnik zunehmend eingesetzt. ⟨B: Beleg für die Zunahme fehlt.⟩
**Gleich geblieben:** die Behauptung einer Zunahme. Sie wird nicht gestrichen (das wäre eine Inhaltsänderung), sondern als belegpflichtig markiert.

### 14. Werbende Wertung (N05)
**Vorher:** …, was sie zu einem unverzichtbaren Werkzeug in der Zahnmedizin und Dermatologie macht.
**Nachher:** … und werden deshalb in der Zahnmedizin und Dermatologie eingesetzt.
**Protokollhinweis:** Die Wertung „unverzichtbar“ entfällt. Soll sie bleiben, braucht sie einen Beleg (B). Diese Entscheidung wird im Änderungsprotokoll offengelegt.

### 15. Schachtelsatz in einer Herleitung (Satzklammer, S)
**Vorher:** Unter der Annahme langsam veränderlicher Amplituden (SVEA) und der Vernachlässigung der zweiten Ableitungen nach Ort und Zeit erhält man nach einer Reihe von Umformungen, auf die an dieser Stelle aus Gründen der Übersichtlichkeit nicht im Einzelnen eingegangen werden soll, das folgende System gekoppelter Differentialgleichungen:
**Nachher:** Unter der Annahme langsam veränderlicher Amplituden (SVEA) und unter Vernachlässigung der zweiten Ableitungen nach Ort und Zeit ergibt sich nach mehreren Umformungen, die hier nicht im Einzelnen ausgeführt werden, das folgende System gekoppelter Differentialgleichungen:
**Gleich geblieben:** beide Annahmen, der Hinweis, dass Zwischenschritte fehlen, und die Formel. Der Satz schrumpft von 44 auf 34 Wörter, und die Satzklammer ist kürzer.
