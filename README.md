# Regressionsanalyse
## Regressionsgerade von zwei Sachen graphisch darstellen.

In diesem Codeabschnitt habe ich einen Code geschriben, der das Visualisieren des Regressionsgerades von zwei Stichproben macht. Wenn Sie fragen, warum eigentlich wir Regressionsgerade brauchen, dann ist es einfach zu erklären, dass wir die Beziehung von zwei Sachen berechnen, herausbringen. Wir nutzen dadurch Varianz, Covarianz, aritmetische Mittelwert uzw., welche mit Statistik zu tun haben. Es könnte auch in der Realität kein Zusammenhang von bestimmte zwei Sachen geben. Doch wir wählen hier die richtige aus.

Ich habe ein Klasse erstellt, die Regression heißt, und die allgemein dem man die benötigte Mittels von Regression bringt.
```
Instanz = Regression([100.1,102,105,110.3],[4,5.4,5.6,8],"Titelx","Titely")
```
Dem Instanz von Regression werden 4 Parameter eingegeben, nämlich Stichprobe1, Stichprobe2, Titel von X und Titel von Y. Man gibt hier die Stichprobe in Form von Liste und die Titeln nämlich in Form von String, nachdem diese gemacht wurde, dann können folgende Funktionen benutzt werden:

```
1- get_residuen() # welche die Abstände zwischen Vermutung und Realität zurückgibt.
2- get_wert(x) # das gibt dem man den Funktionswert von x an.
3- zeichnen() # in der Grafik zeigen.
```
## Output
![Figure_1](https://github.com/Dankeser/Regressionsanalyse/assets/131388485/df9d4dac-5d9c-4deb-ad77-b05c33bae1e1)



