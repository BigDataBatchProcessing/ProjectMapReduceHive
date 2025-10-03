# Zestaw 0 – hotels-reservations

## Program MapReduce (2)

Działając na zbiorze `datasource1` `(1)` należy wyznaczyć liczbę rezerwacji w poszczególnych hotelach dla każdego roku rozpoczęcia rezerwacji, a także średnią cenę w tych grupach.  

W wynikowym zbiorze `(3)` powinny znaleźć się cztery atrybuty:  

* `hotel_id` – identyfikator hotelu,  
* `year` – rok rozpoczęcia (`check-id`) rezerwacji w formacie `YYYY`,  
* `reservation_count` – liczba rezerwacji w danej grupie,  
* `avg_price` – średnia cena rezerwacji.  

---

## Program Hive (5)

Działając na wyniku zadania MapReduce `(3)` oraz zbiorze danych `datasource4` `(4)` należy powiązać dane o rezerwacjach z informacjami o hotelach, a następnie obliczyć ranking hoteli, pod względem stosunku sumarycznej liczby rezerwacji rozpoczętych w roku 2024 do liczby pokoi danego hotelu.  

Dla każdego hotelu należy wyznaczyć jego nazwę, łączną liczbę rezerwacji rozpoczętych w roku 2024, średnią cenę tych rezerwacji, liczbę pokoi w hotelu oraz pozycje w powyżej określonym rankingu.  

Wynik `(6)` powinien zawierać następujące atrybuty:  

* `hotel_name` – nazwa hotelu,  
* `total_reservations` – liczba rezerwacji rozpoczętych w 2024 w tym hotelu,  
* `avg_price` – średnia cena tych rezerwacji,  
* `rooms` – liczba pokoi w hotelu,  
* `rank` – pozycja hotelu w rankingu względem stosunku sumarycznej liczby rezerwacji rozpoczętych w roku 2024 do liczby pokoi danego hotelu.  

Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu – patrz opis projektu na stronie kursu.  
