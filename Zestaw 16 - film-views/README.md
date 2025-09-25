# Zestaw 16 – film-views  

## Program MapReduce (2)  

Działając na zbiorze `datasource1` `(1)` należy wyznaczyć statystyki popularności filmów w ramach poszczególnych platform streamingowych.  

Dane powinny zostać pogrupowane według:  
* identyfikatora filmu (`film_id`),  
* platformy streamingowej (`platform`).  

W ramach każdej grupy należy obliczyć:  
* `total_views` – łączną liczbę odsłon filmu na danej platformie,  
* `avg_watch_time` – średni czas oglądania (w minutach).  

W wynikowym zbiorze `(3)` powinny znaleźć się cztery atrybuty:  
* `film_id` – identyfikator filmu,  
* `platform` – platforma streamingowa,  
* `total_views` – łączna liczba odsłon filmu na danej platformie,  
* `avg_watch_time` – średni czas (w minutach) oglądania filmu na danej platformie.  

---

## Program Hive (5)

Działając na wyniku zadania MapReduce `(3)` oraz zbiorze danych `datasource4` `(4)` należy powiązać dane o odsłonach filmów z informacjami o filmach.

Na podstawie tych danych należy wyliczyć dla każdego filmu średni stosunek czasu oglądania filmu do całkowitej długości filmu (`pct_film_watch_time`) oraz średni stosunek czasu oglądania wszystkich filmów dla tego samego gatunku do całkowitej ich długości (`pct_genre_watch_time`).  

W wyniku chcemy ograniczyć się tylko do tych filmów, dla których `pct_film_watch_time` jest większy niż `pct_genre_watch_time`.

Wynik `(6)` powinien zawierać następujące atrybuty:  

* `genre` – gatunek filmu,  
* `film_title` – tytuł filmu,  
* `total_views` – łączna liczba odsłon filmu na wszystkich platformach,  
* `pct_film_watch_time` – średni stosunek czasu oglądania filmu do całkowitej jego długości,  
* `pct_genre_watch_time` – średni stosunek czasu oglądania wszystkich filmów dla tego gatunku do całkowitej ich długości.  

---

Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu – patrz opis projektu na stronie kursu.
  
