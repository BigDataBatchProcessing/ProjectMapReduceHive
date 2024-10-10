# Zestaw 10 – google-playstore-apps

## Program MapReduce (2)

Działając na zbiorze `datasource1` `(1)` dla każdego developera i każdego roku wydania aplikacji należy wyznaczyć sumę ocen, liczbę ocen oraz liczbę utworzonych przez niego aplikacji. W obliczeniach należy pominąć te aplikacje, które zostały ocenione przez mniej niż 1000 osób.

Uwaga! Przemyśl to w jaki sposób wyznaczysz sumę ocen. Uwzględnij to jaki jest oczekiwany ostateczny wynik przetwarzania.

W wynikowym zbiorze `(3)` powinny znaleźć się atrybuty:

* identyfikator developera
* rok wydania aplikacji
* suma ocen
* liczba ocen
* liczba utworzonych aplikacji

## Program Hive (5)

Działając na wyniku zadania MapReduce `(3)` oraz zbiorze danych `datasource4` `(4)` należy dla każdego roku wydawania
aplikacji wyznaczyć nazwy trzech developerów ocenionych najlepiej przez użytkowników.

Ostateczny wynik `(6)` powinien zawierać następujące atrybuty:

* `developer_name` – nazwa developera
* `year` – rok wydania aplikacji
* `avg_rate` – średnia ocena użytkowników
* `count_apps` – liczba aplikacji
* `count_rates` – liczba ocen

Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu – patrz opis projektu na stronie kursu. 