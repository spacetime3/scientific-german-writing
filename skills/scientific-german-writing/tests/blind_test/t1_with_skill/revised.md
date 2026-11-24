## 2.3 Stimulierte Brillouin-Streuung

Die stimulierte Brillouin-Streuung (SBS) begrenzt die Leistungsskalierung schmalbandiger Faserlaser und -verstärker. Sie ist ein nichtlinearer Prozess: Eine einfallende Pumpwelle regt über Elektrostriktion eine akustische Welle an, an der ein Teil der Pumpleistung in eine rückwärts laufende Stokes-Welle gestreut wird [12].

Die Frequenzverschiebung der Stokes-Welle gegenüber der Pumpwelle ergibt sich aus der Energie- und Impulserhaltung zu $\nu_B = 2 n v_A / \lambda_p$, wobei $n$ den effektiven Brechungsindex, $v_A$ die Schallgeschwindigkeit im Kern und $\lambda_p$ die Pumpwellenlänge bezeichnet. Für Quarzglas mit $n = 1{,}45$ und $v_A = 5960$ m/s erhält man bei 1550 nm eine Brillouin-Verschiebung von etwa 11,1 GHz. Diese Verschiebung ist stets unabhängig von der Dotierung des Faserkerns. ⟨F: Widerspricht der Formel davor: ν_B hängt von n und v_A ab, und beide ändern sich mit der Dotierung (GeO₂ senkt z. B. die Schallgeschwindigkeit im Kern). Bitte prüfen und den Satz streichen oder den Gültigkeitsbereich angeben.⟩

Die Bandbreite des Brillouin-Gewinnspektrums wird durch die Dämpfung der akustischen Phononen bestimmt und beträgt in Standard-Singlemode-Fasern typischerweise 20 bis 30 MHz [13]. Das Gewinnspektrum lässt sich in guter Näherung durch ein Lorentz-Profil beschreiben:

$$g_B(\nu) = g_B^{\max} \frac{(\Delta\nu_B/2)^2}{(\nu-\nu_B)^2 + (\Delta\nu_B/2)^2}. \tag{2.7}$$

Die Schwellleistung wird üblicherweise mit dem Kriterium nach Smith [14] abgeschätzt. Dabei wird die Schwelle als diejenige Pumpleistung definiert, bei der die rückgestreute Stokes-Leistung die transmittierte Pumpleistung am Faserende erreicht. ⟨F: Bezugsorte präzisieren: Bei Smith wird die Stokes-Leistung am Fasereingang mit der Pumpleistung am Faserende verglichen, und die Schwelle ist die eingekoppelte Pumpleistung. Im jetzigen Satz kann sich „am Faserende“ auf beide Leistungen beziehen. Bitte mit [14] abgleichen.⟩ Es ergibt sich näherungsweise

$$P_{\mathrm{th}} \approx 21 \frac{A_{\mathrm{eff}}}{g_B L_{\mathrm{eff}}}, \tag{2.8}$$

wobei $A_{\mathrm{eff}}$ die effektive Modenfläche und $L_{\mathrm{eff}}$ die effektive Wechselwirkungslänge ist. Nach Gleichung (2.8) sinkt die Schwelle mit zunehmender Faserlänge. ⟨F, gering: In Gl. (2.8) steht L_eff, nicht die Faserlänge L; L_eff wächst nur, bis es sich bei großen Längen dem Wert 1/α nähert. Ggf. „mit zunehmender effektiver Wechselwirkungslänge“ schreiben.⟩ Kurze Fasern sind daher für Hochleistungsanwendungen vorteilhaft.
