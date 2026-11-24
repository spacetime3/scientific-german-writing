# Beispiel: Satz-für-Satz-Analyse (Modus S)

Text: `tests/texts/t1_physik_theorie.md`, Abschnitt 2.3 „Stimulierte Brillouin-Streuung“ (theoretische Physik, Masterarbeit).
Vorabscan: `python scripts/scan_text.py tests/texts/t1_physik_theorie.md`

---

### Satz 1.1
1. **Original:** »Die stimulierte Brillouin-Streuung (SBS) spielt eine zentrale Rolle bei der Leistungsskalierung schmalbandiger Faserlaser und -verstärker.«
2. **Schwächen:** E02 „spielt eine zentrale Rolle“ (S, mittel).
3. **Erläuterung:** Die Wendung sagt nicht, welche Rolle. Aus dem Abschnitt (Schwellleistung, Gl. 2.8, „Hochleistungsanwendungen“) geht hervor, dass SBS die Leistung begrenzt.
4. **Vorschlag:** »Die stimulierte Brillouin-Streuung (SBS) begrenzt die Leistungsskalierung schmalbandiger Faserlaser und -verstärker.«
5. **Fachlicher Abgleich:** Gegenstand, Abkürzung und Anwendungsbereich sind identisch. „Begrenzt“ ist eine Konkretisierung, die der Abschnitt selbst begründet, also keine neue Behauptung.
6. **Begründung:** Das Verb trägt jetzt die Aussage, und der Leser weiß sofort, warum SBS behandelt wird.

### Satz 1.2
1. **Original:** »Es handelt sich dabei um einen nichtlinearen Prozess, bei dem eine einfallende Pumpwelle über Elektrostriktion eine akustische Welle anregt, an der ein Teil der Pumpleistung in eine rückwärts laufende Stokes-Welle gestreut wird [12].«
2. **Schwächen:** leicht schwerfälliger Einstieg „Es handelt sich dabei um“ (S, gering); zwei Relativsätze hintereinander.
3. **Erläuterung:** Die Hauptsache (der Mechanismus) steht in den Relativsätzen. Der Hauptsatz enthält nur die Klassifikation.
4. **Vorschlag:** »In diesem nichtlinearen Prozess regt eine einfallende Pumpwelle über Elektrostriktion eine akustische Welle an, an der ein Teil der Pumpleistung in eine rückwärts laufende Stokes-Welle gestreut wird [12].«
5. **Fachlicher Abgleich:** Mechanismus (Elektrostriktion → akustische Welle → Rückstreuung), Richtung (rückwärts) und Verweis [12] am selben Satz sind unverändert.
6. **Begründung:** Der Mechanismus rückt in den Hauptsatz, und der Satz verliert vier Wörter.

### Satz 2.1
1. **Original:** »Die Frequenzverschiebung … ergibt sich aus der Energie- und Impulserhaltung zu $\nu_B = 2 n v_A / \lambda_p$, wobei …«
2. **Schwächen:** keine. **Satz bleibt.** (31 Wörter, aber die Symbolerklärung im *wobei*-Satz ist Standard.)

### Satz 2.2
1. **Original:** »Für Quarzglas mit $n = 1{,}45$ und $v_A = 5960$ m/s erhält man bei 1550 nm eine Brillouin-Verschiebung von etwa 11,1 GHz.«
2. **Schwächen:** keine. **Satz bleibt.** Plausibilitätsrechnung: 2 · 1,45 · 5960 m/s / 1550 nm ≈ 11,15 GHz, passt zu „etwa 11,1 GHz“.

### Satz 2.3
1. **Original:** »Diese Verschiebung ist stets unabhängig von der Dotierung des Faserkerns.«
2. **Schwächen:** V04 „stets“, **Klasse F (hoch)**.
3. **Erläuterung:** Nach der Formel in Satz 2.1 hängt $\nu_B$ von $v_A$ ab. Die Schallgeschwindigkeit hängt von der Glaszusammensetzung ab, also auch von der Dotierung. Der Satz widerspricht damit dem eigenen Text.
4. **Vorschlag:** Satz unverändert + ⟨F: … „stets unabhängig“ bitte prüfen.⟩
5. **Fachlicher Abgleich:** nicht verändert. Die Skill formuliert keine Ersatzaussage.
6. **Begründung:** Eine fachliche Korrektur muss der Autor vornehmen. Eine sprachliche Glättung würde den Fehler nur verdecken.

### Satz 3.1
1. **Original:** »Darüber hinaus ist die Bandbreite des Brillouin-Gewinnspektrums von besonderer Bedeutung.«
2. **Schwächen:** U01 + F03 (S, mittel).
3. **Erläuterung:** „Darüber hinaus“ ist hier formal additiv, aber „von besonderer Bedeutung“ sagt nicht, wofür. Der Satz kündigt nur an, dass jetzt die Bandbreite kommt.
4. **Vorschlag:** »Neben der Frequenzverschiebung charakterisiert die Bandbreite das Brillouin-Gewinnspektrum.«
5. **Fachlicher Abgleich:** Es wird keine Wertung hinzugefügt. Die Bandbreite charakterisiert das Spektrum, was der Folgesatz und Gl. (2.7) bestätigen.
6. **Begründung:** inhaltlicher statt mechanischer Übergang, Anknüpfung an Bekanntes.

### Satz 3.2 / 3.3
**Keine Schwächen. Sätze bleiben.** „typischerweise“ und „in guter Näherung“ sind korrektes Hedging und werden nicht gestrichen.

### Satz 4.1
1. **Original:** »Die Durchführung einer Abschätzung der Schwellleistung erfolgt üblicherweise mit dem Kriterium nach Smith [14].«
2. **Schwächen:** N08 und N02, dreistufige Nominalkette mit Blähverb (S, mittel).
3. **Erläuterung:** „Durchführung“ und „erfolgt“ tragen keine Bedeutung, die Handlung steckt in „Abschätzung“.
4. **Vorschlag:** »Die Schwellleistung wird üblicherweise mit dem Kriterium nach Smith [14] abgeschätzt.«
5. **Fachlicher Abgleich:** „üblicherweise“ und [14] bleiben erhalten, ebenso „Abschätzung“ als abgeschätzt.
6. **Begründung:** 13 statt 15 Wörter, das Verb trägt die Handlung.

### Satz 4.2
1. **Original:** »Dabei wird die Schwelle als diejenige Pumpleistung definiert, bei der …«
2. **Schwächen:** U04 „Dabei“ (S, gering), Bezug ist aber eindeutig.
3. **Erläuterung:** optional. „Dabei“ bezieht sich auf das Kriterium, ein Nomen macht das explizit.
4. **Vorschlag (optional):** »Nach diesem Kriterium ist die Schwelle diejenige Pumpleistung, bei der …«
5. **Fachlicher Abgleich:** Definition wortgleich.
6. **Begründung:** Der Bezug wird explizit. Alternativ ist auch Belassen vertretbar.

### Satz 5.2
1. **Original:** »Gleichung (2.8) verdeutlicht, dass die Schwelle mit zunehmender Faserlänge sinkt, was die Bedeutung kurzer Fasern für Hochleistungsanwendungen unterstreicht.«
2. **Schwächen:** S04/R04 Kommentar-Anhang (S, mittel); Größenverwechslung Faserlänge vs. $L_{\mathrm{eff}}$ (F, mittel).
3. **Erläuterung:** Die Folgerung wird als „Bedeutung“ behauptet statt ausgesprochen. Gl. (2.8) enthält $L_{\mathrm{eff}}$, das für große Längen sättigt.
4. **Vorschlag:** »Nach Gleichung (2.8) sinkt die Schwelle mit zunehmender Faserlänge; für Hochleistungsanwendungen sind daher kurze Fasern günstig.« ⟨F: Gl. (2.8) enthält $L_{\mathrm{eff}}$ …⟩
5. **Fachlicher Abgleich:** Richtung (sinkt) und Folgerung (kurze Fasern) sind aus dem Original übernommen. Die Größenfrage bleibt markiert.
6. **Begründung:** Aussage statt Bedeutungsbehauptung. Die fachliche Unschärfe wird sichtbar, nicht versteckt.

**Integritätsprüfung:** `check_integrity.py` meldet für die Gesamtrevision (`tests/results/t1_revised.md`) 20/20 geschützte Elemente unverändert.
