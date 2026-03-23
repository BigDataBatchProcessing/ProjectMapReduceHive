# Zestaw 22 – shops-reviews

## Program MapReduce (2)

Działając na zbiorze `datasource1` `(1)` należy wyznaczyć miesięczne statystyki ocen
dla każdego sklepu w podziale na miesiące.

Dane powinny zostać pogrupowane według:  
* identyfikatora sklepu (`shop_id`),  
* miesiąca recenzji (`review_month`, wyodrębnionego z `review_date`).  

W ramach każdej grupy należy obliczyć:  
* `avg_rating` – średnią ocenę sklepu w danym miesiącu,  
* `review_count` – liczbę recenzji sklepu w danym miesiącu,  
* `low_rating_count` – liczbę recenzji sklepu z oceną nie wyższą niż 2 w danym miesiącu.  

W wynikowym zbiorze `(3)` powinny znaleźć się następujące atrybuty:  
* `shop_id` – identyfikator sklepu,  
* `review_month` – miesiąc recenzji w formacie `YYYY-MM`,  
* `avg_rating` – średnia ocena sklepu w danym miesiącu,  
* `review_count` – liczba recenzji sklepu w danym miesiącu,  
* `low_rating_count` – liczba recenzji sklepu z oceną nie wyższą niż 2 w danym miesiącu.  

---

## Program Hive (5)

Działając na wyniku zadania MapReduce `(3)` oraz zbiorze danych `datasource4` `(4)` należy
powiązać dane o recenzjach ze słownikiem sklepów, a następnie obliczyć zestawienia na
poziomie regionów i kategorii sklepów.

Pole `products` w `(4)` zawiera listę produktów dostępnych w sklepie — należy je rozwinąć i na tej
podstawie wyznaczyć liczbę unikalnych produktów oferowanych w danej grupie
(`products_in_category`).

Dla każdego regionu i kategorii sklepu należy obliczyć:  
* liczbę unikalnych produktów oferowanych w sklepach tej kategorii w regionie,  
* średnią ocenę wszystkich sklepów w grupie (`region_category_avg_rating`),  
* liczbę sklepów w grupie (`shop_count`),  
* odchylenie średniej oceny w danym regionie i kategorii od średniej oceny dla tej samej
  kategorii we wszystkich regionach (`rating_deviation`).  

Wynik `(6)` powinien zawierać następujące atrybuty:  
* `region` – region sklepu,  
* `category` – kategoria sklepu,  
* `products_in_category` – liczba unikalnych produktów dostępnych w sklepach tej kategorii
  w regionie,  
* `region_category_avg_rating` – średnia ocen wszystkich sklepów w regionie i kategorii,  
* `shop_count` – liczba sklepów w regionie i kategorii,  
* `rating_deviation` – różnica między średnią oceną w danym regionie i kategorii a średnią
  oceną dla tej samej kategorii we wszystkich regionach.  

---

Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu
– patrz opis projektu na stronie kursu.