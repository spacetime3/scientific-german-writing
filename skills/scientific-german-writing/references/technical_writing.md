# Fachspezifische Konventionen: Natur- und Ingenieurwissenschaften

Die Fachkulturen unterscheiden sich darin, wie sie Passiv, „wir“, Nominalstil und Terminologie verwenden. Die Skill passt ihre Empfehlungen an das Fach an und **übernimmt die Konvention des vorliegenden Textes**, solange sie im Fach üblich ist. [R] = eigene Arbeitsregel aus fachüblicher Praxis; formale Regeln zum Formelsatz nach [DIN 1338] (über Hochschulauszüge, siehe `source_references.md`).

## 1. Übergreifende Regeln für technische Texte
- **Geschützte Elemente** (nie verändern): Formeln, Variablen und Indizes (`n_eff`, $A_{\mathrm{eff}}$), Einheiten und Vorsätze, Zahlenwerte einschließlich Dezimalzeichen und Rundung, Gleichungsnummern, Abbildungs-, Tabellen- und Abschnittsnummern, Literaturverweise, Werkstoff- und Gerätebezeichner (Ti-6Al-4V, Er:YAG, SMF-28), Normen (DIN EN ISO …), Abkürzungen nach ihrer Einführung.
- **Formelsatz** [DIN 1338 über TUD/HTW]: Variablen kursiv, Zahlen und Einheiten gerade; zwischen Zahl und Einheit ein (schmales) Leerzeichen („10 mW“), Ausnahme Grad („5,7°“); Prozent mit oder ohne Leerzeichen, im Text einheitlich; beschreibende Indizes gerade ($P_{\mathrm{th}}$), variable Indizes kursiv ($x_i$). Die Skill **meldet** Verstöße als Hinweis (Klasse S, gering), korrigiert aber in Formeln nichts eigenmächtig.
- **Dezimalzeichen:** Im Deutschen das Komma. In LaTeX steht `1{,}45`, und diese Schreibweise bleibt erhalten. Mischformen (1.45 und 1,45) als Konsistenzhinweis melden.
- **Größen statt Zahlenwertgleichungen:** „die Leistung $P = 10$ mW“ ist korrekt. „die Leistung von 10“ ohne Einheit ist ein **F**-Hinweis.
- **Abkürzungen:** beim ersten Auftreten ausschreiben, danach konsistent verwenden. Wechsel zwischen „SBS“ und „Brillouin-Streuung“ nur, wenn der Autor ihn beabsichtigt.
- **Terminologie-Konsistenz:** Größen- und Begriffsnamen (effektive Fläche ≠ Modenfläche ≠ Kernfläche; Faserlänge ≠ effektive Länge) nie synonym variieren. Im Zweifel ist eine Verwechslung ein **F**-Befund.

## 2. Physik (theoretisch und experimentell)
- „wir“ in Herleitungen üblich („Wir betrachten …“, „erhalten wir“); in Experimentalteilen eher Passiv.
- Herleitungsstruktur: Ausgangsgleichung → Annahmen (explizit!) → Umformung → Ergebnis → Gültigkeitsbereich. Fehlende Annahmen sind **L/F**.
- Typische Standardwendungen: „in erster Ordnung“, „unter Vernachlässigung von“, „im Grenzfall“, „für … ≪ …“, „adiabatisch eliminieren“, „langsam veränderliche Amplitude“. Das sind **Termini, keine Floskeln**.
- Häufige Fachfehler zum Markieren: Proportionalitätsrichtung (E ∝ 1/λ), Intensität vs. Leistung, Phasen- vs. Gruppengeschwindigkeit, Frequenz vs. Kreisfrequenz (Faktor 2π), Halbwertsbreite vs. 1/e-Breite.

## 3. Elektrotechnik / Leistungselektronik
- Passiv und Vorgangsbeschreibungen dominieren; Nominalstil in Spezifikationen üblich („Nennbetriebspunkt“, „Schaltfrequenz“).
- Normgerechte Formelzeichen ($U$, $I$, $P_V$, $R_{th,JC}$) und Bauteilbezeichner (IGBT, MOSFET) bleiben unverändert.
- Blähverben („Die Ermittlung erfolgt …“) sind hier besonders verbreitet. Auflösen, wo es lesbarer wird, Fachnomen aber erhalten („Lebensdauerabschätzung“).
- Betriebsbedingungen (Nennbetrieb, transient, Zyklus WLTP) sind Gültigkeitsbereiche und dürfen nicht entfallen.

## 4. Maschinenbau / Werkstofftechnik / Materialwissenschaften
- Vorgangspassiv in Methodik („Die Proben wurden … geglüht“) ist Standard.
- Werkstoffbezeichnungen nach Norm (Ti-6Al-4V, 42CrMo4, AlSi10Mg), Gefügebezeichnungen (α', α+β, martensitisch, lamellar) und Prozessparameter (Volumenenergiedichte) sind geschützte Termini.
- Kennwerte immer mit Prüfbedingung: „Ermüdungsfestigkeit bei R = −1, 10⁷ Zyklen“. Fehlt die Bedingung, **F** (gering) melden, aber nicht ergänzen.
- Häufige Fachfehler: Festigkeit vs. Steifigkeit, Härte vs. Festigkeit, Rauheitskenngrößen (Ra vs. Rz).

## 5. Medizintechnik
- Doppelte Fachsprache (Technik + Medizin). Medizinische Termini (Osseointegration, Koagulation, Ablation) und Normen (DIN EN ISO 13485, IEC 60601) unverändert lassen.
- Wirksamkeitsaussagen („schonend“, „sicher“, „nahezu vollständig vermieden“) sind regulatorisch heikel. Ohne Beleg **B**, bei Übertreibung **F** markieren.
- Keine Verallgemeinerung von Patientengruppen oder Indikationen bei der Überarbeitung.

## 6. Optik und Laserphysik
- Wellenlängen mit Einheit (1550 nm, 2,94 µm), Laserbezeichner (Er:YAG, Nd:YAG, Yb-dotiert), Strahlparameter ($M^2$, BPP), Pulsangaben (fs, ps, ns; Pulsenergie vs. Spitzenleistung vs. mittlere Leistung) sind geschützt. Verwechslungen sind **F**.
- Übliche Wendungen: „im Fernfeld“, „beugungsbegrenzt“, „bei einer Wellenlänge von“, „Modenfeldradius“, „effektive Fläche“, „Schwelle nichtlinearer Prozesse“.
- Häufige Fachfehler: Photonenenergie und Wellenlänge (umgekehrt proportional), Intensität und Fluenz, „Leistung“ für Pulsenergie, 1/e- und 1/e²-Radius.

## 7. Mathematik
- „Es sei …“, „Sei …“, „Dann gilt“, „o. B. d. A.“, „Wir zeigen …“, „Daraus folgt“, „Satz“, „Lemma“, „Beweis“, „∎“: **feste Konventionen, nie als Floskel werten** (F04 Ausnahme).
- „wir“ ist Standard. Präzision geht vor Lesefluss: „genau dann, wenn“ ist nicht „wenn“, und „für alle“ ist nicht „für viele“. Solche Quantoren werden nie geändert.
- Kurze, gleichförmige Sätze sind in Beweisen funktional. Hier keine Rhythmusvariation verlangen.

## 8. Informatik
- „wir“ verbreitet; Aktiv häufig („Der Algorithmus berechnet …“).
- Code, Bezeichner, Funktionsnamen, Komplexitätsangaben ($\mathcal{O}(n \log n)$) und Pseudocode sind geschützt.
- Etablierte Anglizismen (Framework, Deployment, Overfitting, Batch Size) bleiben. Nur unnötige Anglizismen im Fließtext („adressieren“ für „behandeln“) als N07 melden.
- „signifikant“ nur bei statistischem Test, sonst „deutlich“ oder die Zahl.

## 9. Textteil-spezifische Erwartungen
| Textteil | Tempus | Stil | Typische Schwächen |
|---|---|---|---|
| Einleitung | Präsens, Perfekt | Begründung der Relevanz mit Belegen | E01–E06, unbelegte Bedeutung (B) |
| Theorie/Grundlagen | Präsens | Definitionen, Herleitungen, Termini | Nominalketten, fehlende Annahmen, F |
| Methodik | Präteritum (Passiv) | Reproduzierbarkeit | Blähverben, fehlende Parameter |
| Ergebnisse | Präteritum/Präsens | Zahlen, Verweise auf Abb./Tab. | Wertungen statt Werte, Interpretation im Ergebnisteil |
| Diskussion | Präsens | Vergleich, Erklärung, Einschränkung | Hedging-Fehler, Statusverschiebung, A04/A05 |
| Fazit/Ausblick | Präsens, Futur | Antwort auf Zielsetzung | S01–S06, A05 |
