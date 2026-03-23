# Zestaw 19 – stations-weather

## Program MapReduce (2)

Działając na zbiorze `datasource1` `(1)` należy obliczyć miesięczne statystyki pogodowe
dla każdej stacji meteorologicznej.

Dane powinny zostać pogrupowane według:  
* identyfikatora stacji (`station_id`),  
* miesiąca pomiaru (`month`, w formacie `YYYY-MM`).  

W ramach każdej grupy należy obliczyć:  
* `avg_temp` – średnią miesięczną temperaturę na stacji,  
* `max_wind_speed` – maksymalną prędkość wiatru w danym miesiącu na stacji,  
* `stormy_count` – liczbę pomiarów z warunkami `Stormy` w danym miesiącu na stacji.  

W wynikowym zbiorze `(3)` powinny znaleźć się następujące atrybuty:  
* `station_id` – identyfikator stacji,  
* `month` – miesiąc pomiaru (w formacie `YYYY-MM`),  
* `avg_temp` – średnia temperatura na stacji w danym miesiącu,  
* `max_wind_speed` – maksymalna prędkość wiatru na stacji w danym miesiącu,  
* `stormy_count` – liczba pomiarów z warunkami `Stormy` na stacji w danym miesiącu.  

---

## Program Hive (5)

Działając na wyniku zadania MapReduce `(3)` oraz zbiorze danych `datasource4` `(4)` należy
powiązać dane o pomiarach ze słownikiem stacji meteorologicznych, a następnie obliczyć
zestawienia na poziomie regionów i miesięcy.

Dla każdego regionu i miesiąca należy wyznaczyć średnią temperaturę w regionie w danym miesiącu
(`region_month_avg_temp`) oraz średnią temperaturę w regionie obliczoną na podstawie
wszystkich miesięcy (`region_avg_temp`), a także różnicę między tymi wartościami
(`avg_temp_deviation`).

Dodatkowo – w ramach każdego regionu – należy utworzyć ranking stacji według średniej
temperatury. Ranking powinien być reprezentowany jako tablica rekordów, w której każdy
rekord zawiera:  
* `station_id` – identyfikator stacji,  
* `rank_in_region` – pozycję stacji w rankingu w ramach danego regionu.  

Wynik `(6)` powinien zawierać następujące atrybuty:  
* `region` – region administracyjny,  
* `month` – miesiąc pomiaru,  
* `region_month_avg_temp` – średnia temperatura w regionie w danym miesiącu,  
* `region_avg_temp` – średnia temperatura w regionie obliczona na podstawie wszystkich miesięcy,  
* `avg_temp_deviation` – różnica między średnią temperaturą w danym miesiącu a średnią
  temperaturą całego regionu ze wszystkich miesięcy,  
* `stations_ranking` – tablica rekordów `{station_id, rank_in_region}`.  

---

Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu
– patrz opis projektu na stronie kursu.