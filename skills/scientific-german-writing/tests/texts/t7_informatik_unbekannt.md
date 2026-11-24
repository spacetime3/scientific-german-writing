<!-- Testtext T7: Informatik (maschinelles Lernen), nur für den Blindtest erstellt; keine Referenzüberarbeitung vorhanden. Literaturverweise sind Platzhalter. -->

## 3.2 Wahl der Verlustfunktion

Wir betrachten ein binäres Klassifikationsproblem mit stark unausgeglichenen Klassen: Im Trainingsdatensatz sind nur 2,3 % der $N = 48\,000$ Beispiele positiv. Für solche Datensätze ist die Kreuzentropie als Verlustfunktion bekanntlich ungeeignet, da sie die Mehrheitsklasse bevorzugt.

Vor diesem Hintergrund kommt in dieser Arbeit der Focal Loss nach Lin et al. [21] zur Anwendung. Dieser gewichtet gut klassifizierte Beispiele über einen Fokussierungsparameter $\gamma$ herunter:

$$\mathrm{FL}(p_t) = -\alpha_t (1 - p_t)^{\gamma} \log(p_t). \tag{3.4}$$

Für $\gamma = 0$ geht Gl. (3.4) in die gewichtete Kreuzentropie über. Es ist wichtig zu beachten, dass die Wahl von $\gamma$ einen signifikanten Einfluss auf die Konvergenz des Trainings hat. In Vorversuchen erwies sich $\gamma = 2$ als robuster Kompromiss zwischen Konvergenzgeschwindigkeit und Recall auf der Minderheitsklasse, was die Wichtigkeit einer sorgfältigen Hyperparameteroptimierung unterstreicht.

Darüber hinaus spielt auch die Lernrate eine entscheidende Rolle. Wir verwenden den Optimierer AdamW mit einer Anfangslernrate von $3 \cdot 10^{-4}$ und einem Cosine-Annealing-Schedule über 50 Epochen. Zusammenfassend lässt sich sagen, dass die gewählte Konfiguration einen robusten, effizienten und zuverlässigen Trainingsprozess gewährleistet.
