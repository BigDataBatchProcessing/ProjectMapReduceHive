# Zestaw 5 – netflix-prize-data

## Program MapReduce (2)

Działając na zbiorze `datasource1` `(1)` należy dla każdego filmu wyznaczyć liczbę głosów oraz sumę ocen. W wyniku pomijamy te firmy, na które oddano mniej niż 1000 ocen.

W wynikowym zbiorze `(3)` powinny znaleźć się atrybuty:

* identyfikator filmu
* liczba głosów oddanych na film
* suma ocen oddanych na film

## Program Hive (5)

Działając na wyniku zadania MapReduce `(3)` oraz zbiorze danych `datasource4` `(4)` należy wyznaczyć trzy najlepiej oceniane filmy (o największej średniej ocenie) dla każdej dekady produkcji filmów.

Ostateczny wynik `(6)` powinien zawierać następujące atrybuty:

* `tytul_filmu` – tytuł filmu
* `dekada_produkcji` – dekada produkcji filmu
* `srednia_ocena` – średnia ocena filmu


Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu – patrz opis projektu na stronie kursu. 
