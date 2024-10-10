# Zestaw 7 – carstrucks-data

## Program MapReduce (2)

Działając na zbiorze `datasource1` `(1)` należy dla każdego producenta w każdym regionie wyznaczyć liczbę sprzedawanych samochodów oraz ich sumaryczną cenę. Wynik nie ma zawierać tych producentów, którzy w regionie sprzedawali mniej niż 10 samochodów.

W wynikowym zbiorze `(3)` powinny znaleźć się atrybuty:

* identyfikator regionu (`geo_id`)
* nazwa producenta
* liczba samochodów
* sumaryczna kwota

## Program Hive (5)

Działając na wyniku zadania MapReduce `(3)` oraz zbiorze danych `datasource4` `(4)` należy dla każdego stanu wyznaczyć trzech producentów o najwyższej średniej cenie ich samochodów.

Ostateczny wynik `(6)` powinien zawierać następujące atrybuty:

* `state` – symbol stanu
* `manufacturer` – nazwa producenta
* `avg_price` – średnia cena sprzedanych samochodów

Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu – patrz opis projektu na stronie kursu. 