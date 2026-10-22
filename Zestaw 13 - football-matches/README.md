# Zestaw 13 – football-matches

## Program MapReduce (2)

Działając na zbiorze `datasource1` `(1)` należy wyznaczyć podstawowe statystyki drużyn w każdym sezonie.

**Sezon** w formacie `YYYY` należy wyznaczyć na podstawie daty meczu (`date`) w następujący sposób:  
* Jeśli mecz odbył się między 1 sierpnia a 31 grudnia – należy przypisać rok rozpoczęcia jako rok sezonu,  
* Jeśli mecz odbył się między 1 stycznia a 31 lipca – należy przypisać poprzedni rok jako rok rozpoczęcia sezonu.  

Dane powinny zostać pogrupowane według:  
* identyfikatora drużyny (`team_id`),  
* wyznaczonego sezonu (`season`).

W ramach każdej grupy należy obliczyć dwie miary:  
* `matches_played` – liczba rozegranych meczów w sezonie,  
* `avg_goals_per_match` – średnia goli na mecz w sezonie.

W wynikowym zbiorze `(3)` powinny znaleźć się cztery atrybuty:  
* `team_id` – identyfikator drużyny,  
* `season` – wyznaczony sezon,  
* `matches_played` – liczba rozegranych meczów w sezonie,  
* `avg_goals_per_match` – średnia liczba goli na mecz w sezonie.

---

## Program Hive (5)

Działając na wyniku zadania MapReduce `(3)` oraz zbiorze danych `datasource4` `(4)` należy połączyć dane o meczach z informacjami o drużynach, a następnie obliczyć zestawienia na poziomie ligi (`league`).

Dla każdej ligi należy wyznaczyć:  
* łączną liczbę rozegranych meczów (`total_matches`) przez wszystkie drużyny w lidze,  
* średnią liczbę goli na mecz (`avg_goals_per_match`) w lidze.

Dodatkowo, w ramach każdej ligi, należy utworzyć **ranking drużyn (`team_id`)** według liczby rozegranych meczów. Ranking powinien być reprezentowany jako tablica rekordów, w której każdy rekord zawiera:  
* `team_id` – identyfikator drużyny,  
* `rank_in_league` – pozycję drużyny w rankingu w ramach danej ligi.

Wynik `(6)` powinien zawierać następujące atrybuty:  
* `league` – liga,  
* `total_matches` – łączna liczba rozegranych meczów w lidze,  
* `avg_goals_per_match` – średnia liczba goli na mecz w lidze,  
* `teams_ranking` – tablica rekordów `{team_id, rank_in_league}`.

---

## Uwagi

* `avg_goals_per_match` dotyczy bramek strzelonych przez daną drużynę.
* `avg_goals_per_match` dla ligi to średnia po wszystkich meczach drużyn ligi.
* Pozycja 1 w rankingu oznacza najwięcej rozegranych meczów (wszystkie sezony łącznie).
  Równe wartości otrzymują tę samą pozycję, a kolejna pozycja jest pomijana (np. 1, 2, 2, 4).
  Kolejność rekordów w tablicy nie ma znaczenia.
* Wyniki `(3)` i `(6)` mogą zawierać dodatkowe atrybuty, pod warunkiem że zawierają wszystkie atrybuty wymagane.
* Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu – patrz opis projektu na stronie kursu.

