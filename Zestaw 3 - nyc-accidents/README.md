# Zestaw 3 – nyc-accidents

## Program MapReduce (2)

Działając na zbiorze `datasource1` `(1)` należy dla każdej ulicy w zakresie należącym do określonej strefy pocztowej (w przypadku kiedy dla tej samej ulicy istnieją przypadki opisane różnymi strefami pocztowymi, należy je policzyć oddzielnie) wyznaczyć liczbę poszkodowanych z podziałem na typ poszkodowanych (pieszych, rowerzystów i kierowców) oraz charakter obrażeń (ranni, zabici). Wyniki mają być ograniczone tylko do wypadków mających miejsce po 2012 roku i opisanych kodem pocztowym.

W wynikowym zbiorze `(3)` powinny znaleźć się atrybuty:

* ulica,
* nr strefy pocztowej,
* typ poszkodowanych,
* charakter obrażeń,
* liczba poszkodowanych

Uwaga: Każde zdarzenie może być opisane trzema różnymi ulicami. W zależności od tego ile ulic zostało określonych,
dane zdarzenie należy zaliczyć na konto każdej z nich.

## Program Hive (5)
Działając na wyniku zadania MapReduce `(3)` oraz zbiorze danych `datasource4` `(4)` należy dla każdego typu poszkodowanych wyznaczyć trzy ulice leżące na terenie Manhatanu, dla których suma poszkodowanych (zabici+ranni) jest największa.

Wynik `(6)` powinien zawierać następujące atrybuty:

* `street` – ulica
* `person_type` – typ poszkodowanych
* `killed` – liczba zabitych
* `injured` – liczba rannych

Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu – patrz opis projektu na stronie kursu. 