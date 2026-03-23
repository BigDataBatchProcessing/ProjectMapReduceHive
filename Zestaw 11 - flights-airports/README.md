# Zestaw 11 – flights-airports  

## Program MapReduce (2)  

Działając na zbiorze `datasource1` `(1)` należy wyznaczyć statystyki lotów wychodzących z poszczególnych lotnisk w podziale na miesiąc wylotu.

Dane powinny zostać pogrupowane według:  
* identyfikatora lotniska wylotu (`departure_airport_id`),  
* miesiąca wylotu (`departure_month`, wyodrębnionego z `scheduled_departure`).  

W ramach każdej grupy należy obliczyć:  
* `flight_count` – liczbę lotów w danej grupie,  
* `avg_ticket_price` – średnią cenę biletu w USD,  
* `avg_delay_min` – średnie opóźnienie w minutach, wyliczone wyłącznie dla lotów o statusie `Delayed` (jeśli w danej grupie nie ma takich lotów, należy zwrócić `0`).  

W wynikowym zbiorze `(3)` powinny znaleźć się następujące atrybuty:  
* `departure_airport_id` – identyfikator lotniska wylotu,  
* `departure_month` – miesiąc wylotu w formacie `YYYY-MM`,  
* `flight_count` – liczba lotów w danej grupie,  
* `avg_ticket_price` – średnia cena biletu w USD,  
* `avg_delay_min` – średnie opóźnienie lotów ze statusem `Delayed` w danej grupie.  

---

## Program Hive (5)  

Działając na wyniku zadania MapReduce `(3)` oraz zbiorze danych `datasource4` `(4)` należy powiązać dane o lotach z informacjami o lotniskach, a następnie obliczyć zestawienia na poziomie krajów.  

Dla każdego kraju należy wyznaczyć łączną liczbę lotów wychodzących oraz średnią cenę biletu, a następnie – w ramach każdego kontynentu – nadać krajom pozycje w rankingu według liczby lotów oraz obliczyć odchylenie liczby lotów danego kraju od średniej liczby lotów dla wszystkich krajów na tym samym kontynencie.  

Wynik `(6)` powinien zawierać następujące atrybuty:  
* `continent` – kontynent,  
* `country` – kraj,  
* `total_flights` – liczba lotów wychodzących z danego kraju,  
* `avg_ticket_price` – średnia cena biletu w USD dla lotów wychodzących z danego kraju,  
* `rank_in_continent` – pozycja kraju w rankingu liczby lotów w ramach danego kontynentu,  
* `flights_deviation` – różnica między liczbą lotów z danego kraju a średnią liczbą lotów   dla krajów na tym samym kontynencie.  

---

Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu – patrz opis projektu na stronie kursu.