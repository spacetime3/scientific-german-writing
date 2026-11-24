## 2.3 Stimulierte Brillouin-Streuung

Die stimulierte Brillouin-Streuung (SBS) begrenzt die Leistungsskalierung schmalbandiger Faserlaser und -verstärker. In diesem nichtlinearen Prozess regt eine einfallende Pumpwelle über Elektrostriktion eine akustische Welle an, an der ein Teil der Pumpleistung in eine rückwärts laufende Stokes-Welle gestreut wird [12].

Die Frequenzverschiebung der Stokes-Welle gegenüber der Pumpwelle ergibt sich aus der Energie- und Impulserhaltung zu $\nu_B = 2 n v_A / \lambda_p$, wobei $n$ den effektiven Brechungsindex, $v_A$ die Schallgeschwindigkeit im Kern und $\lambda_p$ die Pumpwellenlänge bezeichnet. Für Quarzglas mit $n = 1{,}45$ und $v_A = 5960$ m/s erhält man bei 1550 nm eine Brillouin-Verschiebung von etwa 11,1 GHz. Diese Verschiebung ist stets unabhängig von der Dotierung des Faserkerns. ⟨F: Nach der Gleichung im vorigen Satz hängt die Verschiebung über $v_A$ von der Schallgeschwindigkeit im Kern ab, und diese hängt von der Kernzusammensetzung (z. B. GeO₂-Anteil) ab. Die Aussage „stets unabhängig“ bitte prüfen.⟩

Neben der Frequenzverschiebung charakterisiert die Bandbreite das Brillouin-Gewinnspektrum. Sie wird durch die Dämpfung der akustischen Phononen bestimmt und beträgt in Standard-Singlemode-Fasern typischerweise 20 bis 30 MHz [13]. Das Gewinnspektrum lässt sich in guter Näherung durch ein Lorentz-Profil beschreiben:

$$g_B(\nu) = g_B^{\max} \frac{(\Delta\nu_B/2)^2}{(\nu-\nu_B)^2 + (\Delta\nu_B/2)^2}. \tag{2.7}$$

Die Schwellleistung wird üblicherweise mit dem Kriterium nach Smith [14] abgeschätzt. Nach diesem Kriterium ist die Schwelle diejenige Pumpleistung, bei der die rückgestreute Stokes-Leistung die transmittierte Pumpleistung am Faserende erreicht. ⟨F: Bezugsorte präzisieren: Beim Smith-Kriterium wird üblicherweise die Stokes-Leistung am Fasereingang mit der Pumpleistung am Faserende verglichen; die Schwelle ist die eingekoppelte Pumpleistung. Bitte mit [14] abgleichen. (Befund aus dem Blindtest.)⟩ Es ergibt sich näherungsweise

$$P_{\mathrm{th}} \approx 21 \frac{A_{\mathrm{eff}}}{g_B L_{\mathrm{eff}}}, \tag{2.8}$$

wobei $A_{\mathrm{eff}}$ die effektive Modenfläche und $L_{\mathrm{eff}}$ die effektive Wechselwirkungslänge ist. Nach Gleichung (2.8) sinkt die Schwelle mit zunehmender Faserlänge; für Hochleistungsanwendungen sind daher kurze Fasern günstig. ⟨F: Gl. (2.8) enthält die effektive Länge $L_{\mathrm{eff}}$, nicht die Faserlänge. Bei hoher Dämpfung sättigt $L_{\mathrm{eff}}$. Gegebenenfalls „mit zunehmender effektiver Wechselwirkungslänge“ schreiben.⟩
