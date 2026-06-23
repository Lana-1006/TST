# TST-SmartMeal

## A1 – Unit-Tests

Für A1 habe ich eine Funktion aus meinem Projekt SmartMeal verwendet. Die Funktion berechnet den täglichen Kalorienbedarf abhängig vom Alter. Anschließend habe ich verschiedene Unit-Tests erstellt.
Ich habe zwei normale Fälle getestet. Zusätzlich habe ich überprüft, ob bei einer ungültigen Eingabe eine Exception ausgelöst wird. Dadurch wird sichergestellt, dass die Funktion nicht nur bei normalen Eingaben richtig arbeitet, sondern auch auf Fehler richtig reagiert.

---

## A2 – TDD

Prompt: 
"Gib mir ein einfaches Beispiel für einen ShoppingCart mit TDD."

<img width="1594" height="712" alt="image" src="https://github.com/user-attachments/assets/23dba334-61d6-4324-ae7d-b4cbb8645790" />
<img width="1502" height="801" alt="image" src="https://github.com/user-attachments/assets/1116ebb5-9454-4c81-9a12-6741eb4eb870" />

Kritik: 
Die KI hat mehr Funktionen vorgeschlagen als ich letztendlich umgesetzt habe. Außerdem hat die KI andere Testnamen verwendet. Die Tests waren zwar ähnlich aufgebaut, ich habe die Namen und die Struktur jedoch an meine Bedürfnisse angepasst.
Die KI hat direkt mehrere Funktionen vorgeschlagen. Ich habe mich dagegen auf die ersten drei Schritte konzentriert, da es länger gedauert hat. Dadurch konnte ich den Ablauf des TDD-Prinzips besser nachvollziehen.
Ein weiterer Unterschied ist, dass die KI natürlich keine Git-History mit einzelnen Red-, Green- und Refactor-Schritten erstellt hat. Diese Entwicklungsschritte habe ich dann selbst dokumentiert und durch mehrere Commits nachvollziehbar gemacht.
Letzendlich habe ich die vorgeschlagene Lösung vereinfacht und an die Anforderungen angepasst. 

---

## A3 – Mocking

Für A3 habe ich Mocking verwendet. In meinem Beispiel empfiehlt SmartMeal unterschiedliche Gerichte abhängig vom Wetter.
Dafür gibt es einen WeatherService, der normalerweise Wetterdaten liefern würde. In einer echten Anwendung wäre dieser Dienst eine externe Abhängigkeit. Der Dienst könnte eine Internetverbindung benötigen, langsam sein oder zeitweise nicht erreichbar sein. Dadurch könnten die Tests unzuverlässig werden.
Aus diesem Grund habe ich den WeatherService gemockt. Durch das Mocking konnte ich selbst festlegen, welches Wetter zurückgegeben wird. Dadurch konnte ich gezielt verschiedene Situationen testen.
Wenn das Wetter „warm“ ist, empfiehlt SmartMeal einen Salat. Wenn das Wetter „cold“ ist, empfiehlt SmartMeal eine Suppe.
Durch das Mocking konnten die Tests unabhängig von einem echten Wetterdienst ausgeführt werden. Die Tests sind dadurch schneller und einfacher.

---

