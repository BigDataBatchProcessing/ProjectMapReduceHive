# Zestaw 14 – bus-trips

## Program MapReduce (2)

Działając na zbiorze `datasource1` `(1)` należy wyznaczyć podstawowe statystyki przejazdów
w podziale na operatora i godzinę odjazdu.

Dane powinny zostać pogrupowane według:  
* identyfikatora operatora (`operator_id`),  
* godziny odjazdu (`departure_hour`, wyodrębnionej z `departure_time`).  

W ramach każdej grupy należy obliczyć:  
* `total_passengers` – łączną liczbę pasażerów w grupie,  
* `avg_ticket_price` – średnią cenę biletu w USD w grupie,  
* `cancelled_count` – liczbę przejazdów o statusie `Cancelled` w danej grupie.  

W wynikowym zbiorze `(3)` powinny znaleźć się następujące atrybuty:  
* `operator_id` – identyfikator operatora,  
* `departure_hour` – godzina odjazdu,  
* `total_passengers` – łączna liczba pasażerów w grupie,  
* `avg_ticket_price` – średnia cena biletu w USD,  
* `cancelled_count` – liczba przejazdów o statusie `Cancelled` w danej grupie.  

---

## Program Hive (5)

Działając na wyniku zadania MapReduce `(3)` oraz zbiorze danych `datasource4` `(4)` należy
powiązać dane o przejazdach z informacjami o operatorach, a następnie obliczyć zestawienia
na poziomie regionów i typów usług świadczonych przez operatorów.

Dla każdego regionu i typu usługi należy obliczyć łączną liczbę pasażerów, średnią cenę
biletu oraz współczynnik anulowania przejazdów (`cancelled_ratio`) rozumiany jako udział
przejazdów anulowanych w łącznej liczbie przejazdów. Dodatkowo – w ramach każdego regionu
– należy nadać typom usług pozycje w rankingu według łącznej liczby przewiezionych pasażerów
oraz obliczyć odchylenie liczby pasażerów w danym regionie i typie usługi od średniej liczby
pasażerów dla tego samego typu usługi we wszystkich regionach.

Wynik `(6)` powinien zawierać następujące atrybuty:  
* `region` – region działania operatora,  
* `service_type` – typ świadczonej usługi (np. *Express*, *Local*, *Intercity*),  
* `total_passengers` – łączna liczba pasażerów przewiezionych w regionie w ramach danego
  typu usługi,  
* `avg_ticket_price` – średnia cena biletu w USD,  
* `cancelled_ratio` – udział przejazdów anulowanych w łącznej liczbie przejazdów,  
* `rank_in_region` – pozycja typu usługi w rankingu liczby pasażerów w ramach danego regionu,  
* `passengers_deviation` – różnica między liczbą pasażerów w danym regionie i typie usługi
  a średnią liczbą pasażerów dla tego samego typu usługi we wszystkich regionach.  

---

Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu
– patrz opis projektu na stronie kursu.