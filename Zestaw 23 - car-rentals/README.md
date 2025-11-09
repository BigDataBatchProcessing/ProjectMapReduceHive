# Zestaw 23 - cars-rentals

## Program MapReduce (2)

Działając na zbiorze `datasource1` `(1)` należy obliczyć podstawowe statystyki wypożyczeń samochodów.  

Dane powinny zostać pogrupowane według:  
* identyfikatora samochodu (`car_id`),  
* roku wypożyczenia (`rental_year`).  

W ramach każdej grupy należy obliczyć:  
* `total_rentals` – łączną liczbę wypożyczeń w danym roku dla samochodu,  
* `completed_ratio` – udział wypożyczeń zakończonych statusem `Completed` w stosunku do wszystkich wypożyczeń w danej grupie.  

Wynikowym zbiorze `(3)` powinny znaleźć się następujące atrybuty:  
* `car_id` – identyfikator samochodu,  
* `rental_year` – rok wypożyczenia,  
* `total_rentals` – liczba wypożyczeń dla samochodu w danym roku,  
* `completed_ratio` – udział wypożyczeń zakończonych statusem `Completed`.  

---

## Program Hive (5)

Działając na wyniku zadania MapReduce `(3)` oraz zbiorze danych `datasource4` `(4)` należy powiązać dane o wypożyczeniach ze słownikiem samochodów.

Na podstawie tych danych należy wyliczyć, dla każdej kombinacji cecha samochodu (`feature`) i roku (`rental_year`):  
* `feature_year_avg_rentals` – średnia liczba wypożyczeń samochodów w grupie cecha + rok,  
* `feature_year_avg_completed_ratio` – średni udział wypożyczeń zakończonych statusem `Completed` w przypadku samochodów w grupie cecha + rok,  
* `above_avg_rentals` – flaga logiczna (`true/false`), określająca, czy średnia liczba wypożyczeń w grupie cecha + rok jest wyższa niż średnia liczba wypożyczeń dla tej cechy biorąc pod uwagę wszystkie lata.

Wynik `(6)` powinien zawierać następujące atrybuty:  
* `feature` – cecha samochodu,  
* `rental_year` – rok wypożyczenia,  
* `feature_year_avg_rentals` – średnia liczba wypożyczeń samochodów w grupie cecha + rok,  
* `feature_year_avg_completed_ratio` – średni udział wypożyczeń zakończonych statusem `Completed` w grupie cecha + rok,  
* `above_avg_rentals` – flaga logiczna (`true/false`), określająca, czy liczba wypożyczeń w grupie cecha + rok jest wyższa niż średnia dla danej cechy we wszystkich latach. 

---

Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu – patrz opis projektu na stronie kursu.
