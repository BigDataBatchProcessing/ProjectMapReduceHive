# Zestaw 2 – nyc-taxi

## Program MapReduce (2)

Działając na zbiorze `datasource1` `(1)` należy dla każdego miesiąca (w określonym roku) wyznaczyć liczbę pasażerów, którzy wsiedli do taksówek w poszczególnych strefach (strefa włączenia taksometru) i opłacili swój przejazd gotówką.

W wynikowym zbiorze `(3)` powinny znaleźć się atrybuty:

* miesiąc,
* strefa rozpoczęcia podróży oraz
* liczba pasażerów, jaka rozpoczęła swoją podróż w podanej strefie w podanym miesiącu

## Program Hive (5)

Działając na wyniku zadania MapReduce `(3)` oraz zbiorze danych `datasource4` `(4)` należy dla każdego miesiąca wyznaczyć
trzy dzielnice (Borough), w których wsiadło najwięcej pasażerów.

Wynik `(6)` powinien zawierać następujące atrybuty:

* `month` – miesiąc
* `borough` – dzielnica
* `passengers` – liczba pasażerów jaka rozpoczęła swoją podróż w podanej dzielnicy w podanym miesiącu

Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu – patrz opis projektu na stronie kursu. 