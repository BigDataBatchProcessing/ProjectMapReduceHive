# Zestaw 4 – imdb-persons

## Program MapReduce (2)

Działając na zbiorze `datasource1` `(1)` należy dla każdej osoby wyznaczyć liczbę filmów, w których te osoby zagrały oraz liczbę filmów, które te osoby wyreżyserowały.

Uwaga: Przez osoby, które zagrały w filmach rozumiemy osoby oznaczone jako aktorzy (`actor`), aktorki (`actress`), a także osoby, które zagrały samych siebie (`self`).

W wynikowym zbiorze `(3)` powinny znaleźć się atrybuty:
* identyfikator osoby (`nconst`) oraz
* liczba filmów, w jakich ta osoba zagrała
* liczba filmów, które ta osoba wyreżyserowała

## Program Hive (5)
Działając na wyniku zadania MapReduce `(3)` oraz zbiorze danych `datasource4` `(4)` należy wyznaczyć trzech aktorów – osoby których główną profesją jest aktorstwo (w rolach wymienionych w `primaryProfession` znajduje się jedna z wartości {`actress`, `actor`}), które zagrały w największej liczbie filmów oraz trzech reżyserów – osoby których
główną profesją jest reżyseria (w rolach wymienionych w `primaryProfession` znajduje się {`director`}), które wyreżyserowały największą liczbę filmów.

Ostateczny wynik `(6)` powinien zawierać następujące atrybuty:

* primaryName – nazwa aktora
* role – czy reżyser, czy aktor
* movies – liczba filmów 

Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu – patrz opis projektu na stronie kursu. 