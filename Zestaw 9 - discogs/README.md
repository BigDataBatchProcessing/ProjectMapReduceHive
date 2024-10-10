# Zestaw 9 – discogs

## Program MapReduce (2)

Działając na zbiorze `datasource1` `(1)` należy dla każdej wytwórni, każdego artysty, w każdej dekadzie, wyznaczyć liczbę wydanych płyt oraz lista różnych gatunków, których te płyty dotyczyły.

W wynikowym zbiorze `(3)` powinny znaleźć się atrybuty:

* identyfikator wytwórni
* identyfikator artysty
* nazwa artysty
* dekada
* liczba wydanych płyt
* lista różnych gatunków na wydanych płytach

## Program Hive (5)

Działając na wyniku zadania MapReduce `(3)` oraz zbiorze danych `datasource4` `(4)` należy wyznaczyć dla każdej dekady te trzy wytwórnie, które wydały największą liczbę płyt.

Ostateczny wynik `(6)` powinien zawierać następujące atrybuty:

* `label_name` – nazwa wytwórni
* `decade` – dekada
* `artists_count` – liczba artystów wydanych płyt
* `releases_count` – liczba wydanych płyt
* `genres` – lista różnych gatunków na wydanych płytach 

Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu – patrz opis projektu na stronie kursu. 