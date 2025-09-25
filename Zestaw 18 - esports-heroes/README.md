# Zestaw 18 – esports-heroes

## Program MapReduce (2)

Działając na zbiorze `datasource1` `(1)` należy wyznaczyć podstawowe statystyki graczy w poszczególnych rozgrywkach z użyciem konkretnych bohaterów.

Dane powinny zostać pogrupowane według:  
* identyfikatora gracza (`player_id`),  
* nazwy użytego bohatera (`hero_name`).

W ramach każdej grupy należy obliczyć trzy miary dotyczące wyników rozgrywek tego gracza z użyciem tego bohatera:  
* `wins` – łączna liczba zwycięstw,  
* `draws` – łączna liczba remisów,  
* `losses` – łączna liczba porażek.

W wynikowym zbiorze `(3)` powinny znaleźć się następujące atrybuty:  
* `player_id` – identyfikator gracza,  
* `hero_name` – nazwa bohatera,  
* `wins` – liczba zwycięstw dla tej kombinacji gracz–bohater,  
* `draws` – liczba remisów dla tej kombinacji gracz–bohater,  
* `losses` – liczba porażek dla tej kombinacji gracz–bohater.

---

## Program Hive (5)

Działając na wyniku zadania MapReduce `(3)` oraz zbiorze danych `datasource4` `(4)` należy powiązać dane o rozgrywkach z informacjami dotyczących graczy.

Na podstawie tych danych należy wyliczyć, dla każdego regionu i bohatera:  
* łączną liczbę zwycięstw (`total_wins`),  
* łączną liczbę remisów (`total_draws`),  
* łączną liczbę porażek (`total_losses`).

Ponadto, dla każdego bohatera, należy wyznaczyć średnią liczbę zwycięstw we wszystkich regionach i oznaczyć, które kombinacje region–bohater mają liczbę zwycięstw większą od tej średniej.

Wynik `(6)` powinien zawierać następujące atrybuty:  
* `region` – region graczy,  
* `hero_name` – nazwa bohatera,  
* `total_wins` – łączna liczba zwycięstw dla bohatera w regionie,  
* `total_draws` – łączna liczba remisów dla bohatera w regionie,  
* `total_losses` – łączna liczba porażek dla bohatera w regionie,  
* `above_avg_wins` – flaga logiczna (`true/false`), określająca, czy liczba zwycięstw tego bohatera w regionie jest wyższa niż średnia liczba zwycięstw tego bohatera we wszystkich regionach.

---

Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu – patrz opis projektu na stronie kursu.
