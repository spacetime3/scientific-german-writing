## 3.2 Wahl der Verlustfunktion

Wir betrachten ein binäres Klassifikationsproblem mit stark unausgeglichenen Klassen: Im Trainingsdatensatz sind nur 2,3 % der $N = 48\,000$ Beispiele positiv. Für solche Datensätze ist die Kreuzentropie als Verlustfunktion ungeeignet, da sie die Mehrheitsklasse bevorzugt. ⟨B: Beleg fehlt, etwa Lin et al. [21], falls die Aussage dort steht.⟩ ⟨F: „ungeeignet“ ist absolut formuliert. Die Kreuzentropie wird bei unausgeglichenen Klassen auch mit Klassengewichtung oder Resampling eingesetzt. Ist die ungewichtete Kreuzentropie gemeint, oder „nur eingeschränkt geeignet“?⟩

Vor diesem Hintergrund verwenden wir in dieser Arbeit den Focal Loss nach Lin et al. [21]. Dieser gewichtet gut klassifizierte Beispiele über einen Fokussierungsparameter $\gamma$ herunter:

$$\mathrm{FL}(p_t) = -\alpha_t (1 - p_t)^{\gamma} \log(p_t). \tag{3.4}$$

⟨F: $p_t$ und $\alpha_t$ werden hier nicht erklärt. Falls sie nicht bereits früher definiert sind, nach der Gleichung ergänzen.⟩

Für $\gamma = 0$ geht Gl. (3.4) in die gewichtete Kreuzentropie über. Die Wahl von $\gamma$ beeinflusst die Konvergenz des Trainings deutlich. In Vorversuchen erwies sich $\gamma = 2$ als robuster Kompromiss zwischen Konvergenzgeschwindigkeit und Recall auf der Minderheitsklasse. ⟨B: Vorversuche dokumentieren: getestete Werte von γ, Ergebnisse, Verweis auf Tabelle oder Anhang.⟩ ⟨F: „robust“ wogegen? Gegenüber Zufallsinitialisierung (Seeds), Datensplits oder benachbarten γ-Werten?⟩

Neben dem Fokussierungsparameter beeinflusst auch die Lernrate das Training entscheidend. ⟨F: Inwiefern? Konvergenzgeschwindigkeit, Stabilität, erreichter Recall? Ohne diese Angabe bleibt die Aussage unbestimmt.⟩ Wir verwenden den Optimierer AdamW mit einer Anfangslernrate von $3 \cdot 10^{-4}$ und einem Cosine-Annealing-Schedule über 50 Epochen.
