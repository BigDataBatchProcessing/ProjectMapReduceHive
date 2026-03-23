# Zestaw 18 – esports-heroes

## Program MapReduce (2)

Działając na zbiorze `datasource1` `(1)` należy wyznaczyć podstawowe statystyki graczy
w poszczególnych rozgrywkach z użyciem konkretnych bohaterów.

Dane powinny zostać pogrupowane według:  
* identyfikatora gracza (`player_id`),  
* nazwy użytego bohatera (`hero_name`).  

W ramach każdej grupy należy obliczyć:  
* `wins` – łączną liczbę zwycięstw,  
* `draws` – łączną liczbę remisów,  
* `losses` – łączną liczbę porażek,  
* `dominant_wins` – liczbę zwycięstw, w których gracz uzyskał więcej zabójstw niż śmierci.  

W wynikowym zbiorze `(3)` powinny znaleźć się następujące atrybuty:  
* `player_id` – identyfikator gracza,  
* `hero_name` – nazwa bohatera,  
* `wins` – liczba zwycięstw dla tej kombinacji gracz–bohater,  
* `draws` – liczba remisów dla tej kombinacji gracz–bohater,  
* `losses` – liczba porażek dla tej kombinacji gracz–bohater,  
* `dominant_wins` – liczba zwycięstw z przewagą zabójstw nad śmierciami dla tej kombinacji
  gracz–bohater.  

---

## Program Hive (5)

Działając na wyniku zadania MapReduce `(3)` oraz zbiorze danych `datasource4` `(4)` należy
powiązać dane o rozgrywkach z informacjami dotyczącymi graczy, a następnie obliczyć
zestawienia na poziomie regionów i bohaterów.

Dla każdego regionu i bohatera należy obliczyć łączną liczbę zwycięstw (`total_wins`),
remisów (`total_draws`), porażek (`total_losses`) oraz łączną liczbę dominujących zwycięstw
(`total_dominant_wins`). Ponadto, dla każdego bohatera, należy wyznaczyć średnią liczbę
zwycięstw we wszystkich regionach i oznaczyć, które kombinacje region–bohater mają liczbę
zwycięstw większą od tej średniej (`above_avg_wins`).

Dodatkowo – w ramach każdego regionu – należy utworzyć ranking bohaterów według łącznej
liczby zwycięstw. Ranking powinien być reprezentowany jako tablica rekordów, w której każdy
rekord zawiera:  
* `hero_name` – nazwę bohatera,  
* `rank_in_region` – pozycję bohatera w rankingu w ramach danego regionu.  

Wynik `(6)` powinien zawierać następujące atrybuty:  
* `region` – region graczy,  
* `hero_name` – nazwa bohatera,  
* `total_wins` – łączna liczba zwycięstw dla bohatera w regionie,  
* `total_draws` – łączna liczba remisów dla bohatera w regionie,  
* `total_losses` – łączna liczba porażek dla bohatera w regionie,  
* `total_dominant_wins` – łączna liczba dominujących zwycięstw dla bohatera w regionie,  
* `above_avg_wins` – flaga logiczna (`true/false`), określająca, czy liczba zwycięstw tego
  bohatera w regionie jest wyższa niż średnia liczba zwycięstw tego bohatera we wszystkich
  regionach,  
* `heroes_ranking` – tablica rekordów `{hero_name, rank_in_region}`.  

---

Cyfry w nawiasach odnoszą się do cyfr wykorzystowanych na graficznej reprezentacji projektu
– patrz opis projektu na stronie kursu.