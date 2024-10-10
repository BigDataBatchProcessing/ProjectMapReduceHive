# Zestaw 1 – imdb-genres

## Program MapReduce (2)

Działając na zbiorze `datasource1` `(1)` należy wyznaczyć liczbę aktorów, którzy zagrali w poszczególnych filmach.

Uwaga: Przez aktorów rozumiemy osoby oznaczone jako aktorzy (`actor`), aktorki (`actress`), a także osoby, które
zagrały samych siebie (`self`).

W wynikowym zbiorze `(3)` powinny znaleźć się dwa atrybuty:

* identyfikator filmu oraz
* liczba aktorów, jaka w tym filmie zagrała

## Program Hive (5)

Działając na wyniku zadania MapReduce oraz zbiorze danych `datasource4` `(4)` należy wyznaczyć trzy gatunki (genres)
wśród filmów długometrażowych (titleType=movie), w których została zaangażowana największa liczba aktorów.

Filmy, które mają określonych wiele gatunków należy zaliczyć do każdego z nich.

Wynik `(6)` powinien zawierać następujące atrybuty:

* `genre` – gatunek
* `movies` – liczba filmów
* `actors` – liczba aktorów

Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu – patrz opis projektu na stronie kursu. 