# Zestaw 12 – sales-products  

## Program MapReduce (2)  

Działając na zbiorze `datasource1` `(1)` należy obliczyć zagregowane informacje o sprzedaży
w podziale na produkt i rok transakcji.  

Dane powinny zostać pogrupowane według:  
* identyfikatora produktu (`product_id`),  
* roku transakcji (`transaction_year`, wyodrębnionego z `transaction_time`).  

W ramach każdej grupy należy obliczyć:  
* `total_quantity` – łączną liczbę sprzedanych sztuk,  
* `avg_unit_price` – średnią cenę jednostkową produktu,  
* `mobile_quantity` – łączną liczbę sztuk sprzedanych z użyciem metody płatności `Mobile`.  

W wynikowym zbiorze `(3)` powinny znaleźć się następujące atrybuty:  
* `product_id` – identyfikator produktu,  
* `transaction_year` – rok transakcji,  
* `total_quantity` – łączna liczba sprzedanych sztuk,  
* `avg_unit_price` – średnia cena jednostkowa produktu,  
* `mobile_quantity` – łączna liczba sztuk sprzedanych z użyciem metody płatności `Mobile`.  

---

## Program Hive (5)  

Działając na wyniku zadania MapReduce `(3)` oraz zbiorze danych `datasource4` `(4)` należy
połączyć dane transakcji z informacjami o produktach, a następnie obliczyć zestawienia
na poziomie kategorii produktów.  

Dla każdej kategorii należy wyznaczyć:  
* łączną liczbę sprzedanych sztuk (`total_quantity`),  
* średnią cenę jednostkową (`avg_unit_price`),  
* łączną liczbę sztuk sprzedanych z użyciem metody płatności `Mobile` (`mobile_quantity_total`).  

Dodatkowo, w ramach każdej kategorii, należy utworzyć ranking marek (`brand`) według łącznej
liczby sprzedanych sztuk. Ranking powinien być reprezentowany jako tablica rekordów,
w której każdy rekord zawiera:  
* `brand` – nazwę marki,  
* `rank_in_category` – pozycję marki w rankingu w ramach danej kategorii.  

Wynik `(6)` powinien zawierać następujące atrybuty:  
* `category` – kategoria produktu,  
* `total_quantity` – łączna liczba sprzedanych sztuk w kategorii,  
* `avg_unit_price` – średnia cena jednostkowa w kategorii,  
* `mobile_quantity_total` – łączna liczba sztuk sprzedanych z użyciem metody płatności `Mobile`
  w kategorii,  
* `brands_ranking` – tablica rekordów `{brand, rank_in_category}`.  

---

Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu
– patrz opis projektu na stronie kursu.