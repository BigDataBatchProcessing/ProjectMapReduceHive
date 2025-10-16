# Zestaw 21 – parks-visits

## Program MapReduce (2)

Działając na zbiorze `datasource1` `(1)` należy obliczyć statystyki wizyt dla każdego parku w poszczególnych dniach.  

Dane powinny zostać pogrupowane według:  
* identyfikatora parku (`park_id`),  
* daty wizyty (`date`).  

W ramach każdej grupy należy obliczyć:  
* `visits_count` – łączną liczbę wizyt w danym parku w danym dniu,  
* `avg_group_size` – średnią liczebność grup odwiedzających.  

W wynikowym zbiorze `(3)` powinny znaleźć się następujące atrybuty:  
* `park_id` – identyfikator parku,  
* `date` – data wizyty (dzień),  
* `visits_count` – liczba wizyt w danym dniu,  
* `avg_group_size` – średnia wielkość grup odwiedzających w danym dniu.  

---

## Program Hive (5)

Działając na wyniku zadania MapReduce `(3)` oraz zbiorze danych `datasource4` `(4)` należy powiązać dane o wizytach ze słownikiem parków.  

Na podstawie tych danych należy wyliczyć, dla każdego typu przyrody (`nature_types`) i regionu:  
* łączną liczbę wizyt (`total_visits`),  
* średnią wielkość grup (`avg_group_size`).  

Ponadto należy obliczyć, dla każdego typu przyrody, odchylenie liczby wizyt w danym regionie od średniej liczby wizyt we wszystkich regionach (`visits_deviation`).  

Wynik `(6)` powinien zawierać następujące atrybuty:  
* `nature_type` – typ przyrody (np. Forest, Desert, Coast),  
* `region` – region parku,  
* `total_visits` – łączna liczba wizyt w parkach tego typu w regionie,  
* `avg_group_size` – średnia wielkość grup w parkach tego typu w regionie,  
* `visits_deviation` – różnica między liczbą wizyt w regionie a średnią liczbą wizyt dla danego typu przyrody we wszystkich regionach.  

---

Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu – patrz opis projektu na stronie kursu.
