# Beispiel: Absatzanalyse (Modus P)

## Absatz A – Ingenieurtext (T2, Absatz 1)

**Original:**
> Im Rahmen der vorliegenden Arbeit erfolgt die Durchführung der thermischen Auslegung des Wechselrichtermoduls auf Grundlage eines Cauer-Netzwerks. Die Ermittlung der Verlustleistung der Halbleiterschalter findet dabei unter Berücksichtigung der Schalt- und Durchlassverluste statt, wobei die Bestimmung der Schaltverluste anhand der Datenblattangaben des Herstellers zur Anwendung kommt.

**Funktion des Absatzes:** Methodik: Modell (Cauer-Netzwerk) → Eingangsgröße (Verlustleistung) → Datenquelle.

**Prüfung:**
- *Logischer Zusammenhang:* korrekt, aber die Logik (Modell braucht Verlustleistung als Eingang) ist hinter Nominalketten versteckt.
- *Informationsreihenfolge:* gut (Modell → Eingang → Quelle).
- *Argumentationsstruktur:* rein beschreibend, das ist im Methodenteil angemessen.
- *Wiederholungen:* „Ermittlung“, „Bestimmung“ und „Durchführung“ bezeichnen dreimal dieselbe Tätigkeit.
- *Übergänge:* „dabei“ ist unscharf, „wobei“ hängt eine Hauptinformation an.
- *Terminologie:* konsistent (Schaltverluste, Durchlassverluste, Halbleiterschalter).
- *Erklärung vs. Begründung:* Die Wahl des Cauer-Netzwerks wird nicht begründet. Das ist kein Sprachproblem. Optionaler Hinweis an den Autor: ⟨Autor: Warum Cauer statt Foster? Ein Halbsatz genügt.⟩
- *Scan:* E07, N08 (2×), N02, N03, N01; 4 Nominalisierungen pro Satz.

**Überarbeitet:**
> Das Wechselrichtermodul wird auf Grundlage eines Cauer-Netzwerks thermisch ausgelegt. Die Verlustleistung der Halbleiterschalter setzt sich aus Schalt- und Durchlassverlusten zusammen; die Schaltverluste werden aus den Datenblattangaben des Herstellers bestimmt.

**Was inhaltlich gleich geblieben ist:** Modell, Gegenstand, beide Verlustanteile, Datenquelle. Gestrichen wurde nur „Im Rahmen der vorliegenden Arbeit“, weil es im Kapitel 4.2 einer Arbeit redundant ist. Wörter: 45 → 29 (Scan-Zählung).

---

## Absatz B – Text mit Floskeln (T3, Absatz 2)

**Original:**
> Darüber hinaus ist hervorzuheben, dass ultrakurze Laserpulse eine besonders präzise, schonende und effiziente Materialbearbeitung ermöglichen. Studien zeigen, dass die thermische Schädigung des umliegenden Gewebes bei Pulsdauern im Femtosekundenbereich nahezu vollständig vermieden werden kann. Da die Photonenenergie mit zunehmender Wellenlänge steigt, eignen sich infrarote Laser besonders gut für die Ablation harter Gewebe. Dies unterstreicht die Bedeutung einer sorgfältigen Parameterwahl.

**Funktion des Absatzes:** Eigenschaften der Laserparameter, und zwar Pulsdauer (Satz 1–2) und Wellenlänge (Satz 3), mit einem Fazit (Satz 4).

**Prüfung:**
- *Logischer Zusammenhang:* Satz 1–2 hängen zusammen (Pulsdauer → geringe Schädigung). Satz 3 wechselt das Thema (Wellenlänge) ohne Übergang. Satz 4 bezieht sich mit „Dies“ unklar auf Satz 3 oder den ganzen Absatz (R08).
- *Argumentationsstruktur:* Behauptung (S1) → angeblicher Beleg ohne Quelle (S2, **B**) → fachlich falsche Begründung (S3, **F**) → Bedeutungsfloskel (S4).
- *Wiederholungen:* „präzise“ und „schonend“ greifen dem Satz 2 vor.
- *Übergänge:* „Darüber hinaus ist hervorzuheben“ (U01 + F02) ist mechanisch.
- *Terminologie:* „Materialbearbeitung“ vs. „Ablation“ vs. „Gewebe“: In der Medizintechnik ist „Gewebeabtrag“ oder „Ablation“ präziser als „Materialbearbeitung“. Das ist nur ein Hinweis, denn der Begriff stammt vom Autor.
- *Erklärung vs. Begründung:* Satz 3 gibt eine Begründung, die nicht stimmt. Satz 4 gibt weder Erklärung noch Begründung.

**Überarbeitet:**
> Ultrakurze Laserpulse ermöglichen eine besonders präzise, schonende und effiziente Materialbearbeitung. ⟨B: Beleg für „schonend“ und „effizient“?⟩ Bei Pulsdauern im Femtosekundenbereich lässt sich die thermische Schädigung des umliegenden Gewebes nahezu vollständig vermeiden. ⟨B: Im Original „Studien zeigen“ ohne Quelle, bitte belegen.⟩ Da die Photonenenergie mit zunehmender Wellenlänge steigt, eignen sich infrarote Laser besonders gut für die Ablation harter Gewebe. ⟨F: Photonenenergie sinkt mit der Wellenlänge ($E = hc/\lambda$); vermutlich ist die Wasserabsorption gemeint.⟩

**Was inhaltlich gleich geblieben ist:** alle drei Sachbehauptungen (auch die fehlerhafte, denn sie ist markiert und nicht umgeschrieben), „nahezu vollständig“, „Femtosekundenbereich“. Gestrichen wurden die Floskeln in Satz 1 und der inhaltsleere Satz 4 („unterstreicht die Bedeutung“). Die Triade „präzise, schonende und effiziente“ bleibt, weil das Streichen unbelegter Attribute eine inhaltliche Entscheidung des Autors ist. Sie ist als B markiert.

**Empfehlung an den Autor (nicht umgesetzt):** Absatz in zwei Teile trennen, Pulsdauer und Wellenlänge, und die Wellenlängenbegründung mit Absatz 3 (Wasserabsorption bei 2,94 µm) zusammenführen.
