# Zestaw 15 – food-orders-restaurants  

## Program MapReduce (2)  

Działając na zbiorze `datasource1` `(1)` należy wyznaczyć statystyki zamówień w restauracjach,
w podziale na typ płatności oraz rok złożenia zamówienia.  

Dane powinny zostać pogrupowane według:  
* identyfikatora restauracji (`restaurant_id`),  
* typu płatności (`payment_type`),  
* roku złożenia zamówienia (`order_year`, wyodrębnionego z `order_date`).  

W ramach każdej grupy należy obliczyć:  
* `orders_count` – liczbę zamówień w danej grupie,  
* `avg_total_price` – średnią wartość zamówienia w USD,  
* `cancelled_count` – liczbę zamówień o statusie `Cancelled` w danej grupie.  

W wynikowym zbiorze `(3)` powinny znaleźć się następujące atrybuty:  
* `restaurant_id` – identyfikator restauracji,  
* `payment_type` – typ płatności (np. *Cash*, *Card*, *Online*),  
* `order_year` – rok złożenia zamówienia,  
* `orders_count` – liczba zamówień w danej grupie,  
* `avg_total_price` – średnia wartość zamówienia w USD,  
* `cancelled_count` – liczba zamówień o statusie `Cancelled` w danej grupie.  

---

## Program Hive (5)  

Działając na wyniku zadania MapReduce `(3)` oraz zbiorze danych `datasource4` `(4)` należy
powiązać dane o zamówieniach z informacjami o restauracjach, a następnie obliczyć
zestawienia na poziomie krajów i rodzajów kuchni.  

Dla każdego kraju i rodzaju kuchni należy obliczyć łączną liczbę zamówień, średnią wartość
zamówienia oraz współczynnik anulowania zamówień (`cancelled_ratio`) rozumiany jako udział
zamówień anulowanych w łącznej liczbie zamówień. Dodatkowo – w ramach każdego kraju –
należy nadać rodzajom kuchni pozycje w rankingu według liczby zamówień oraz obliczyć
odchylenie liczby zamówień danego rodzaju kuchni od średniej liczby zamówień dla wszystkich
rodzajów kuchni w tym samym kraju.  

Wynik `(6)` powinien zawierać następujące atrybuty:  
* `country` – kraj,  
* `cuisine` – rodzaj kuchni (np. *Italian*, *Chinese*, *Mexican*),  
* `total_orders` – łączna liczba zamówień w kraju dla danego rodzaju kuchni,  
* `avg_total_price` – średnia wartość zamówienia w USD,  
* `cancelled_ratio` – udział zamówień anulowanych w łącznej liczbie zamówień,  
* `rank_in_country` – pozycja rodzaju kuchni w rankingu liczby zamówień w ramach danego kraju,  
* `orders_deviation` – różnica między liczbą zamówień danego rodzaju kuchni a średnią liczbą
  zamówień dla wszystkich rodzajów kuchni w tym samym kraju.  

---

Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu
– patrz opis projektu na stronie kursu.