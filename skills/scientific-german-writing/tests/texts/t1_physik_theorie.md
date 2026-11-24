<!-- Testtext T1: theoretischer Physiktext (nichtlineare Faseroptik). Literaturverweise sind Platzhalter. -->

## 2.3 Stimulierte Brillouin-Streuung

Die stimulierte Brillouin-Streuung (SBS) spielt eine zentrale Rolle bei der Leistungsskalierung schmalbandiger Faserlaser und -verstärker. Es handelt sich dabei um einen nichtlinearen Prozess, bei dem eine einfallende Pumpwelle über Elektrostriktion eine akustische Welle anregt, an der ein Teil der Pumpleistung in eine rückwärts laufende Stokes-Welle gestreut wird [12].

Die Frequenzverschiebung der Stokes-Welle gegenüber der Pumpwelle ergibt sich aus der Energie- und Impulserhaltung zu $\nu_B = 2 n v_A / \lambda_p$, wobei $n$ den effektiven Brechungsindex, $v_A$ die Schallgeschwindigkeit im Kern und $\lambda_p$ die Pumpwellenlänge bezeichnet. Für Quarzglas mit $n = 1{,}45$ und $v_A = 5960$ m/s erhält man bei 1550 nm eine Brillouin-Verschiebung von etwa 11,1 GHz. Diese Verschiebung ist stets unabhängig von der Dotierung des Faserkerns.

Darüber hinaus ist die Bandbreite des Brillouin-Gewinnspektrums von besonderer Bedeutung. Sie wird durch die Dämpfung der akustischen Phononen bestimmt und beträgt in Standard-Singlemode-Fasern typischerweise 20 bis 30 MHz [13]. Das Gewinnspektrum lässt sich in guter Näherung durch ein Lorentz-Profil beschreiben:

$$g_B(\nu) = g_B^{\max} \frac{(\Delta\nu_B/2)^2}{(\nu-\nu_B)^2 + (\Delta\nu_B/2)^2}. \tag{2.7}$$

Die Durchführung einer Abschätzung der Schwellleistung erfolgt üblicherweise mit dem Kriterium nach Smith [14]. Dabei wird die Schwelle als diejenige Pumpleistung definiert, bei der die rückgestreute Stokes-Leistung die transmittierte Pumpleistung am Faserende erreicht. Es ergibt sich näherungsweise

$$P_{\mathrm{th}} \approx 21 \frac{A_{\mathrm{eff}}}{g_B L_{\mathrm{eff}}}, \tag{2.8}$$

wobei $A_{\mathrm{eff}}$ die effektive Modenfläche und $L_{\mathrm{eff}}$ die effektive Wechselwirkungslänge ist. Gleichung (2.8) verdeutlicht, dass die Schwelle mit zunehmender Faserlänge sinkt, was die Bedeutung kurzer Fasern für Hochleistungsanwendungen unterstreicht.
