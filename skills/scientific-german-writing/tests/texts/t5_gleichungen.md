<!-- Testtext T5: Text mit komplexen Gleichungen (gekoppelte Wellengleichungen). Literaturverweise sind Platzhalter. -->

## 2.4 Gekoppelte Amplitudengleichungen

Zur Beschreibung der Wechselwirkung zwischen Pump-, Stokes- und akustischer Welle wird zunächst die Wellengleichung für das elektrische Feld in Verbindung mit der Navier-Stokes-Gleichung für die Dichteänderung herangezogen. Unter der Annahme langsam veränderlicher Amplituden (SVEA) und der Vernachlässigung der zweiten Ableitungen nach Ort und Zeit erhält man nach einer Reihe von Umformungen, auf die an dieser Stelle aus Gründen der Übersichtlichkeit nicht im Einzelnen eingegangen werden soll, das folgende System gekoppelter Differentialgleichungen:

\begin{align}
\frac{\partial A_p}{\partial z} + \frac{n}{c}\frac{\partial A_p}{\partial t} &= -\frac{\alpha}{2} A_p + i \kappa_1 \rho A_s, \tag{2.10}\\
-\frac{\partial A_s}{\partial z} + \frac{n}{c}\frac{\partial A_s}{\partial t} &= -\frac{\alpha}{2} A_s + i \kappa_1 \rho^* A_p, \tag{2.11}\\
\frac{\partial \rho}{\partial t} + \frac{\Gamma_B}{2} \rho &= i \kappa_2 A_p A_s^* + f(z,t). \tag{2.12}
\end{align}

Hierbei bezeichnen $A_p$ und $A_s$ die Einhüllenden von Pump- und Stokes-Welle, $\rho$ die Amplitude der Dichteschwankung, $\Gamma_B = 2\pi \Delta\nu_B$ die Phononen-Dämpfungsrate und $f(z,t)$ einen Langevin-Rauschterm, welcher die thermische Anregung der akustischen Phononen beschreibt [5]. Die Kopplungskonstanten $\kappa_1$ und $\kappa_2$ hängen vom elektrostriktiven Koeffizienten $\gamma_e$ und der mittleren Dichte $\rho_0$ ab.

Da die Phononenlebensdauer $\tau_B = 1/\Gamma_B$ mit etwa 10 ns deutlich kürzer ist als die typische Dauer der hier betrachteten Pumppulse, kann im stationären Fall die zeitliche Ableitung in Gl. (2.12) vernachlässigt werden. Damit lässt sich $\rho$ adiabatisch eliminieren, und man erhält nach Einsetzen in Gl. (2.10) und (2.11) die bekannten gekoppelten Intensitätsgleichungen

$$\frac{dI_p}{dz} = -g_B I_p I_s - \alpha I_p, \qquad -\frac{dI_s}{dz} = g_B I_p I_s - \alpha I_s. \tag{2.13}$$
