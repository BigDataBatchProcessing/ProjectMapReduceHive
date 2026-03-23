# Zestaw 16 – film-views

## Program MapReduce (2)

Działając na zbiorze `datasource1` `(1)` należy wyznaczyć statystyki popularności filmów
w ramach poszczególnych platform streamingowych.

Dane powinny zostać pogrupowane według:  
* identyfikatora filmu (`film_id`),  
* platformy streamingowej (`platform`).  

W ramach każdej grupy należy obliczyć:  
* `total_views` – łączną liczbę odsłon filmu na danej platformie,  
* `avg_watch_time` – średni czas oglądania w sekundach,  
* `high_rating_count` – liczbę odsłon z oceną nie niższą niż 4 w danej grupie,  
* `countries` – listę unikalnych krajów, z których oglądano film na danej platformie.  

W wynikowym zbiorze `(3)` powinny znaleźć się następujące atrybuty:  
* `film_id` – identyfikator filmu,  
* `platform` – platforma streamingowa,  
* `total_views` – łączna liczba odsłon filmu na danej platformie,  
* `avg_watch_time` – średni czas oglądania w sekundach,  
* `high_rating_count` – liczba odsłon z oceną nie niższą niż 4 w danej grupie,  
* `countries` – lista unikalnych krajów, z których oglądano film na danej platformie.  

---

## Program Hive (5)

Działając na wyniku zadania MapReduce `(3)` oraz zbiorze danych `datasource4` `(4)` należy
powiązać dane o odsłonach filmów z informacjami o filmach.

Pole `countries` zawiera listę krajów — należy je rozwinąć i na tej podstawie wyznaczyć
liczbę unikalnych krajów, z których oglądano filmy danego gatunku (`unique_countries_count`).

Na podstawie tych danych należy wyliczyć dla każdego filmu średni stosunek czasu oglądania
filmu do całkowitej długości filmu (`pct_film_watch_time`) oraz średni stosunek czasu
oglądania wszystkich filmów dla tego samego gatunku do całkowitej ich długości
(`pct_genre_watch_time`).

W wyniku należy ograniczyć się tylko do tych filmów, dla których `pct_film_watch_time`
jest większy niż `pct_genre_watch_time`.

Wynik `(6)` powinien zawierać następujące atrybuty:  
* `genre` – gatunek filmu,  
* `film_title` – tytuł filmu,  
* `total_views` – łączna liczba odsłon filmu na wszystkich platformach,  
* `high_rating_count` – łączna liczba odsłon z oceną nie niższą niż 4,  
* `unique_countries_count` – liczba unikalnych krajów, z których oglądano filmy danego
  gatunku,  
* `pct_film_watch_time` – średni stosunek czasu oglądania filmu do całkowitej jego długości,  
* `pct_genre_watch_time` – średni stosunek czasu oglądania wszystkich filmów dla tego
  gatunku do całkowitej ich długości.  

---

Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu
– patrz opis projektu na stronie kursu.