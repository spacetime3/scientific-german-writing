<!-- Testtext T2: ingenieurwissenschaftlicher Text (Leistungselektronik/Wärmemanagement). Literaturverweise sind Platzhalter. -->

## 4.2 Thermische Auslegung des Wechselrichtermoduls

Im Rahmen der vorliegenden Arbeit erfolgt die Durchführung der thermischen Auslegung des Wechselrichtermoduls auf Grundlage eines Cauer-Netzwerks. Die Ermittlung der Verlustleistung der Halbleiterschalter findet dabei unter Berücksichtigung der Schalt- und Durchlassverluste statt, wobei die Bestimmung der Schaltverluste anhand der Datenblattangaben des Herstellers zur Anwendung kommt.

Für den Nennbetriebspunkt mit einem Phasenstrom von 150 A und einer Schaltfrequenz von 10 kHz ergibt sich pro IGBT eine Gesamtverlustleistung von 212 W. Die Sperrschichttemperatur darf laut Datenblatt 150 °C nicht überschreiten. Bei einer Kühlmitteltemperatur von 65 °C steht somit ein Temperaturhub von 85 K zur Verfügung, der sich auf die thermischen Widerstände zwischen Sperrschicht und Kühlmittel aufteilt (Tab. 4.1).

Die Kühlung des Moduls erfolgt über eine Pin-Fin-Kühlplatte, die von einem Wasser-Glykol-Gemisch durchströmt wird. Der thermische Widerstand zwischen Gehäuse und Kühlmittel hängt dabei stark vom Volumenstrom ab. Bei einem Volumenstrom von 8 l/min wurde in der Messung ein Wert von 0,11 K/W ermittelt, was eine ausreichende Reserve gegenüber dem Auslegungswert von 0,15 K/W darstellt.

Es zeigt sich, dass das Modul im Nennbetrieb thermisch unkritisch ist. Bei transienten Lastwechseln, wie sie im Fahrzyklus WLTP auftreten, kann es jedoch zu Temperaturschwankungen von bis zu 40 K kommen, die die Lebensdauer der Bonddrähte begrenzen [27]. Eine Lebensdauerabschätzung wird in Abschnitt 4.4 vorgenommen.
