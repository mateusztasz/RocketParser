# Rocket Parser

## Opis
Aplikacja dostarcza parser danych dla zbioru zawierającego  orbitalne uruchomienia satelit.

## Typ danych wejściowych
Zbiór danych do parsowania w formie pliku `.txt` jest dostępny pod tym [linkiem](http://planet4589.org/space/log/launchlog.txt).
Dodatkowy opis tabel z pliku można znaleźć pod następującym [linkiem](http://planet4589.org/space/log/launch.html).

## API
Funkcja `group_by(stream, field, filter)` jest główną funkcją, która parsuje plik. Jej zadaniem jest
również zliczanie ilości uruchomień orbitalnych i filtracja wyników na podstawie
daty (rok - `year` i miesiąc `month`). Parser udostępnia również możliwość wyselekcjonowania udanych lub nieudanych
prób orbitalnych za pomocą opcji `filter`  w wywołaniu funkcji.

## Sposób użycia modułu
```python
from RocketParser.RocketParser import RocketParser

parser = RocketParser()
result_dict = parser.group_by(open("launchlog.txt"), 'month', filter=False)

print("JSON format: ", result_dict[0])
print("Python dictionary format: ", result_dict[1])
```

## Uruchomienie aplikacji
Najlepiej poniższą instrukcję wykonać w cmd/terminalu. Ze względu na wizualizację,
w Python IDLE aplikacja może działać niepoprawnie. Wynika to z faktu, że IDLE nie jest systemową linią komend.

```
python RocketParser.py
```
## Uruchomienie testów
```
python -m unittest
```
