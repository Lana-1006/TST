# TST-E1 – SmartMeal

## A1 – Unit-Tests

Für A1 habe ich eine Funktion aus meinem Projekt SmartMeal verwendet. Die Funktion berechnet den täglichen Kalorienbedarf abhängig vom Alter. Anschließend habe ich verschiedene Unit-Tests erstellt.
Ich habe zwei normale Fälle getestet. Zusätzlich habe ich überprüft, ob bei einer ungültigen Eingabe eine Exception ausgelöst wird. Dadurch wird sichergestellt, dass die Funktion nicht nur bei normalen Eingaben richtig arbeitet, sondern auch auf Fehler richtig reagiert.

---

## A2 – Test Driven Development (TDD)


---

## A3 – Mocking

Für A3 habe ich Mocking verwendet. In meinem Beispiel empfiehlt SmartMeal unterschiedliche Gerichte abhängig vom Wetter.
Dafür gibt es einen WeatherService, der normalerweise Wetterdaten liefern würde. In einer echten Anwendung wäre dieser Dienst eine externe Abhängigkeit. Der Dienst könnte eine Internetverbindung benötigen, langsam sein oder zeitweise nicht erreichbar sein. Dadurch könnten die Tests unzuverlässig werden.
Aus diesem Grund habe ich den WeatherService gemockt. Durch das Mocking konnte ich selbst festlegen, welches Wetter zurückgegeben wird. Dadurch konnte ich gezielt verschiedene Situationen testen.
Wenn das Wetter „warm“ ist, empfiehlt SmartMeal einen Salat. Wenn das Wetter „cold“ ist, empfiehlt SmartMeal eine Suppe.
Durch das Mocking konnten die Tests unabhängig von einem echten Wetterdienst ausgeführt werden. Die Tests sind dadurch schneller, einfacher und zuverlässiger.

---

## Testdurchlauf

Alle Tests wurden mit pytest ausgeführt.

Verwendeter Befehl:

```text
python -m pytest -v
```

Ergebnis:

```text
5 passed
```

Alle Tests wurden erfolgreich ausgeführt.
