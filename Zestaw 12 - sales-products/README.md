# Zestaw 12 – sales-products  

## Program MapReduce (2)  

Działając na zbiorze `datasource1` `(1)` należy obliczyć zagregowane informacje o sprzedaży.  

Dane powinny zostać pogrupowane według:  
* identyfikatora produktu oraz  
* rodzaju płatności.  

W ramach każdej grupy należy obliczyć dwie miary:  
* łączną liczbę sprzedanych sztuk (`SUM(quantity)`),  
* średnią wartość jednostkowej ceny (`AVG(unit_price)`).  

W wynikowym zbiorze `(3)` powinny znaleźć się cztery atrybuty:  
* `product_id` – identyfikator produktu,  
* `payment_type` – typ płatności,  
* `total_quantity` – liczba sprzedanych sztuk,  
* `avg_unit_price` – średnia cena jednostkowa.  

---

## Program Hive (5)  

Działając na wyniku zadania MapReduce `(3)` oraz zbiorze danych `datasource4` `(4)` należy połączyć dane transakcji z informacjami o produktach, a następnie obliczyć zestawienia na poziomie kategorii produktów.  

Dla każdej kategorii należy wyznaczyć:  
* łączną liczbę sprzedanych sztuk (`total_quantity`),  
* średnią cenę jednostkową (`avg_unit_price`).  

Dodatkowo, w ramach każdej kategorii, należy utworzyć **ranking marek (`brand`)** według liczby sprzedanych sztuk. Ranking marek powinien być reprezentowany jako tablica rekordów, w której każdy rekord zawiera:  
* `brand` – nazwę marki,  
* `rank_in_category` – pozycję marki w rankingu w ramach danej kategorii.  

Wynik `(6)` powinien zawierać następujące atrybuty:  
* `category` – kategoria produktu,  
* `total_quantity` – liczba sprzedanych sztuk w kategorii,  
* `avg_unit_price` – średnia cena jednostkowa w kategorii,  
* `brands_ranking` – tablica rekordów `{brand, rank_in_category}`.  

---

Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu – patrz opis projektu na stronie kursu.  
