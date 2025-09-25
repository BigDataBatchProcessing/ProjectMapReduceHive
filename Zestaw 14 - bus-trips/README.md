# Zestaw 14 – bus-trips

## Program MapReduce (2)

Działając na zbiorze `datasource1` `(1)` należy wyznaczyć podstawowe statystyki przejazdów w podziale na operatora i godzinę odjazdu.

Dane powinny zostać pogrupowane według:  
* identyfikatora operatora (`operator_id`),  
* godziny odjazdu (`departure_hour`, np. 16, 17, …, 22).

W ramach każdej grupy należy obliczyć dwie miary:  
* `total_passengers` – łączna liczba pasażerów w grupie,  
* `avg_ticket_price` – średnia cena biletu w USD w grupie.

Wynikowym zbiorze `(3)` powinny znaleźć się następujące atrybuty:  
* `operator_id` – identyfikator operatora,  
* `departure_hour` – godzina odjazdu,  
* `total_passengers` – łączna liczba pasażerów w grupie,  
* `avg_ticket_price` – średnia cena biletu w USD.

---

## Program Hive (5)

Działając na wyniku zadania MapReduce `(3)` oraz zbiorze danych `datasource4` `(4)` należy powiązać dane o przejazdach z informacjami o operatorach.

Na podstawie tych danych należy wyliczyć zestawienia na poziomie regionów i typów usług świadczonych przez operatorów.

Dla każdego regionu i typu usługi należy obliczyć:  
* łączną liczbę pasażerów przewiezionych przez operatorów w regionie,  
* średnią cenę biletu w regionie.

Dodatkowo – w ramach każdego regionu – należy nadać operatorom pozycje w rankingu według liczby przewiezionych pasażerów.

Wynik `(6)` powinien zawierać następujące atrybuty:  
* `region` – region działania operatora,  
* `service_type` – typ świadczonej usługi (np. *Express*, *Local*, *Intercity*),  
* `total_passengers` – łączna liczba pasażerów przewiezionych w regionie w ramach danego typu usługi,  
* `avg_ticket_price` – średnia cena biletu w USD,  
* `rank_in_region` – pozycja typu usługi w rankingu liczby przewiezionych pasażerów w ramach danego regionu.

---

Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu – patrz opis projektu na stronie kursu.
