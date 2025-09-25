# Zestaw 22 - shops-reviews

## Program MapReduce (2)

Działając na zbiorze `datasource1` `(1)` należy wyznaczyć miesięczne statystyki ocen dla każdego sklepu.

Dane powinny zostać pogrupowane według:  
* identyfikatora sklepu (`shop_id`),  
* miesiąca (w formacie `YYYY-MM`) pochodzącego z daty recenzji (`review_month`).  

W ramach każdej grupy należy obliczyć:  
* `avg_rating` – średnią ocenę sklepu w danym miesiącu,  
* `review_count` – liczbę recenzji w tym miesiącu.  

W wynikowym zbiorze `(3)` powinny znaleźć się następujące atrybuty:  
* `shop_id` – identyfikator sklepu,  
* `review_month` – miesiąc recenzji (np. `2025-09`),  
* `avg_rating` – średnia ocena sklepu w tym miesiącu,  
* `review_count` – liczba recenzji sklepu w tym miesiącu.  

---

## Program Hive (5)

Działając na wyniku zadania MapReduce `(3)` oraz zbiorze danych `datasource4` `(4)` należy powiązać dane o recenzjach ze słownikiem sklepów.

Na podstawie tych danych należy wyliczyć, dla każdego regionu i kategorii sklepu:  
* liczbę unikalnych produktów oferowanych w tej grupie (`products_in_category`),  
* średnią ocenę wszystkich sklepów w grupie (`region_category_avg_rating`),  
* liczbę sklepów w grupie (`shop_count`).  

Wynik `(6)` powinien zawierać następujące atrybuty:  
* `region` – region sklepu,  
* `category` – kategoria sklepu,  
* `products_in_category` – liczba unikalnych produktów dostępnych w sklepach tej kategorii w regionie,  
* `region_category_avg_rating` – średnia ocen wszystkich sklepów w regionie i kategorii,  
* `shop_count` – liczba sklepów w regionie i kategorii.  

---

Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu – patrz opis projektu na stronie kursu.
