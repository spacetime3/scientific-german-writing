## 4.2 Thermische Auslegung des Wechselrichtermoduls

Das Wechselrichtermodul wird auf Grundlage eines Cauer-Netzwerks thermisch ausgelegt. Die Verlustleistung der Halbleiterschalter setzt sich aus Schalt- und Durchlassverlusten zusammen; die Schaltverluste werden aus den Datenblattangaben des Herstellers bestimmt.

Für den Nennbetriebspunkt mit einem Phasenstrom von 150 A und einer Schaltfrequenz von 10 kHz ergibt sich pro IGBT eine Gesamtverlustleistung von 212 W. Die Sperrschichttemperatur darf laut Datenblatt 150 °C nicht überschreiten. Bei einer Kühlmitteltemperatur von 65 °C steht somit ein Temperaturhub von 85 K zur Verfügung, der sich auf die thermischen Widerstände zwischen Sperrschicht und Kühlmittel aufteilt (Tab. 4.1).

Das Modul wird über eine Pin-Fin-Kühlplatte gekühlt, die von einem Wasser-Glykol-Gemisch durchströmt wird. Der thermische Widerstand zwischen Gehäuse und Kühlmittel hängt stark vom Volumenstrom ab. Bei einem Volumenstrom von 8 l/min wurde ein Wert von 0,11 K/W gemessen; gegenüber dem Auslegungswert von 0,15 K/W bleibt damit eine ausreichende Reserve.

Im Nennbetrieb ist das Modul damit thermisch unkritisch. Bei transienten Lastwechseln, wie sie im Fahrzyklus WLTP auftreten, können jedoch Temperaturschwankungen von bis zu 40 K auftreten, die die Lebensdauer der Bonddrähte begrenzen [27]. Die Lebensdauer wird in Abschnitt 4.4 abgeschätzt.
