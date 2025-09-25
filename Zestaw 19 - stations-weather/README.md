# Zestaw 19 - stations-weather

## Program MapReduce (2)

Działając na zbiorze `datasource1` `(1)` należy obliczyć dzienne statystyki pogodowe dla każdej stacji meteorologicznej.  

Dane powinny zostać pogrupowane według:  
* identyfikatora stacji (`station_id`),  
* daty pomiaru (bez godziny, `date`).  

W ramach każdej grupy należy obliczyć:  
* `avg_temp` – średnią dzienną temperaturę na stacji,  
* `max_wind_speed` – maksymalną prędkość wiatru w danym dniu na stacji.  

W wynikowym zbiorze `(3)` powinny znaleźć się następujące atrybuty:  
* `station_id` – identyfikator stacji,  
* `date` – data pomiaru (dzień),  
* `avg_temp` – średnia temperatura na stacji w danym dniu,  
* `max_wind_speed` – maksymalna prędkość wiatru na stacji w danym dniu.  

---

## Program Hive (5)

Działając na wyniku zadania MapReduce `(3)` oraz zbiorze danych `datasource4` `(4)` należy powiązać dane o pomiarach ze słownikiem stacji meteorologicznych.  

Na podstawie tych danych należy wyliczyć, dla każdego regionu i dnia:  
* średnią temperaturę w regionie w danym dniu (`region_day_avg_temp`),  
* średnią temperaturę w regionie we wszystkich dniach (`region_avg_temp`),  
* różnicę między tymi wartościami (`avg_temp_deviation`).  

Wynik `(6)` powinien zawierać następujące atrybuty:  
* `region` – region administracyjny,  
* `date` – dzień pomiaru,  
* `region_day_avg_temp` – średnia temperatura w regionie w danym dniu,  
* `region_avg_temp` – średnia temperatura w regionie obliczona na podstawie wszystkich dni,  
* `avg_temp_deviation` – różnica między średnią temperaturą w danym dniu a średnią temperaturą całego regionu.  

---

Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu – patrz opis projektu na stronie kursu.  
