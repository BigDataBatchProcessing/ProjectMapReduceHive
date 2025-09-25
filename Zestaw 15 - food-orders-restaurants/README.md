# Zestaw 15 – food-orders-restaurants  

## Program MapReduce (2)  

Działając na zbiorze `datasource1` `(1)` należy wyznaczyć statystyki zamówień w restauracjach, w podziale na typ płatności.  

Dane powinny zostać pogrupowane według:  
* identyfikatora restauracji (`restaurant_id`),  
* typu płatności (`payment_type`).  

W ramach każdej grupy należy obliczyć:  
* `orders_count` – liczbę zamówień w danej grupie,  
* `avg_total_price` – średnią wartość zamówienia w USD.  

W wynikowym zbiorze `(3)` powinny znaleźć się cztery atrybuty:  
* `restaurant_id` – identyfikator restauracji,  
* `payment_type` – typ płatności (np. *Cash*, *Card*, *Online*),  
* `orders_count` – liczba zamówień w grupie,  
* `avg_total_price` – średnia wartość zamówienia w USD.  

---

## Program Hive (5)  

Działając na wyniku zadania MapReduce `(3)` oraz zbiorze danych `datasource4` `(4)` należy powiązać dane o zamówieniach z informacjami o restauracjach.  

Na podstawie tych danych należy wyliczyć zestawienia na poziomie krajów i rodzajów kuchni.  

Dla każdego kraju i rodzaju kuchni należy obliczyć:  
* łączną liczbę zamówień,  
* średnią wartość zamówienia.  

Dodatkowo – w ramach każdego kraju – należy nadać rodzajom kuchni pozycje w rankingu według liczby zamówień.  

Wynik `(6)` powinien zawierać następujące atrybuty:  
* `country` – kraj,  
* `cuisine` – rodzaj kuchni (np. *Italian*, *Chinese*, *Mexican*),  
* `total_orders` – łączna liczba zamówień w kraju dla danej kuchni,  
* `avg_total_price` – średnia wartość zamówienia w USD,  
* `rank_in_country` – pozycja rodzaju kuchni w rankingu liczby zamówień w ramach danego kraju.  

---

Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu – patrz opis projektu na stronie kursu.
