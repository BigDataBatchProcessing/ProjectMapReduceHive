# Zestaw 8 – flight-delays

## Program MapReduce (2)

Działając na zbiorze `datasource1` `(1)` należy dla każdego lotniska docelowego i każdego miesiąca wyznaczyć liczbę lądowań, oraz ich sumaryczne opóźnienie. W obliczeniach należy pominąć loty odwołane.

W wynikowym zbiorze `(3)` powinny znaleźć się atrybuty:

* identyfikator lotniska (`DESTINATION_AIRPORT`)
* rok
* miesiąc
* liczba lądowań
* sumaryczne opóźnienie

## Program Hive (5)

Działając na wyniku zadania MapReduce `(3)` oraz zbiorze danych `datasource4` `(4)` należy dla każdego miesiąca wyznaczyć
trzy stany o największym średnim opóźnieniu przylotów.

Ostateczny wynik `(6)` powinien zawierać następujące atrybuty:

* `year` - rok
* `month` – miesiąc
* `state` – nazwa stanu
* `avg_delay` – średnie opóźnienie

Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu – patrz opis projektu na stronie kursu. 