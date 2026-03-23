# Zestaw 0 – hotels-reservations

## Program MapReduce (2)

Działając na zbiorze `datasource1` `(1)` należy wyznaczyć statystyki rezerwacji
w poszczególnych hotelach w podziale na rok rozpoczęcia rezerwacji.

Dane powinny zostać pogrupowane według:  
* identyfikatora hotelu (`hotel_id`),  
* roku rozpoczęcia rezerwacji (`year`, wyodrębnionego z `check_in`).  

W ramach każdej grupy należy obliczyć:  
* `reservation_count` – liczbę rezerwacji w danej grupie,  
* `avg_price` – średnią cenę rezerwacji,  
* `cancelled_count` – liczbę rezerwacji o statusie `Cancelled` w danej grupie.  

W wynikowym zbiorze `(3)` powinny znaleźć się następujące atrybuty:  

* `hotel_id` – identyfikator hotelu,  
* `year` – rok rozpoczęcia rezerwacji w formacie `YYYY`,  
* `reservation_count` – liczba rezerwacji w danej grupie,  
* `avg_price` – średnia cena rezerwacji,  
* `cancelled_count` – liczba rezerwacji o statusie `Cancelled` w danej grupie.  

---

## Program Hive (5)

Działając na wyniku zadania MapReduce `(3)` oraz zbiorze danych `datasource4` `(4)` należy
powiązać dane o rezerwacjach z informacjami o hotelach, a następnie obliczyć ranking hoteli
pod względem stosunku łącznej liczby rezerwacji rozpoczętych w roku 2024 do liczby pokoi
danego hotelu.

Dla każdego hotelu należy wyznaczyć łączną liczbę rezerwacji rozpoczętych w roku 2024,
średnią cenę tych rezerwacji, współczynnik anulowania rezerwacji (`cancelled_ratio`)
rozumiany jako udział rezerwacji anulowanych w łącznej liczbie rezerwacji, liczbę pokoi
oraz pozycję w powyżej określonym rankingu.

Wynik `(6)` powinien zawierać następujące atrybuty:  

* `hotel_name` – nazwa hotelu,  
* `total_reservations` – liczba rezerwacji rozpoczętych w 2024 roku w danym hotelu,  
* `avg_price` – średnia cena tych rezerwacji,  
* `cancelled_ratio` – udział rezerwacji anulowanych w łącznej liczbie rezerwacji,  
* `rooms` – liczba pokoi w hotelu,  
* `rank` – pozycja hotelu w rankingu według stosunku łącznej liczby rezerwacji rozpoczętych
  w roku 2024 do liczby pokoi danego hotelu.  

---

Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu
– patrz opis projektu na stronie kursu.