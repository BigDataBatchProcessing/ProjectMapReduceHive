# Zestaw 11 – flights-airports  

## Program MapReduce (2)  

Działając na zbiorze `datasource1` `(1)` należy wyznaczyć liczbę lotów wychodzących z poszczególnych lotnisk w podziale na status lotu, a także średnią cenę biletu w tych grupach.  

W wynikowym zbiorze `(3)` powinny znaleźć się cztery atrybuty:  

* `departure_airport_id` – identyfikator lotniska wylotu,  
* `status` – status lotu (np. *On time*, *Delayed*, *Cancelled*),  
* `flight_count` – liczba lotów w danej grupie,  
* `avg_ticket_price` – średnia cena biletu w USD.  

---

## Program Hive (5)  

Działając na wyniku zadania MapReduce oraz zbiorze danych `datasource4` `(4)` należy powiązać dane o lotach z informacjami o lotniskach, a następnie obliczyć zestawienia na poziomie krajów.  

Dla każdego kraju należy wyznaczyć łączną liczbę lotów oraz średnią cenę biletu, a następnie – w ramach każdego kontynentu – nadać krajom pozycje w rankingu według liczby lotów.  

Wynik `(6)` powinien zawierać następujące atrybuty:  

* `continent` – kontynent,  
* `country` – kraj,  
* `total_flights` – liczba lotów wychodzących z danego kraju,  
* `avg_ticket_price` – średnia cena biletu dla lotów z danego kraju,  
* `rank_in_continent` – pozycja kraju w rankingu liczby lotów w ramach danego kontynentu.  

---

Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu – patrz opis projektu na stronie kursu.