# Oczekiwane wyniki dla danych testowych 2025-01

Poniżej zamieszczone zostały oczekiwane wyniki dla zestawów danych `2025-02` dla poszczególnych ze zestawów projektów. 

Uwaga! 
* Poniższe wyniki należy wykorzystywać, do ewentualnej weryfikacji wyników uzyskiwanych w projekcie 2 podczas jego IMPLEMENTACJI. 
* Podczas dokonywania RECENZJI zostanie dostarczony nowy komplet zestawów danych. 

Poniżej dla każdego etapu podano 
* liczbę wierszy wyniku oraz 
* postać pierwszego "rekordu". Kolejność została określona w oparciu rosnące wartości: 
    - dla *MapReduce* - składowych klucza (zgodnie z ich kolejnością wymienioną w opisie)
    - dla *Hive* - wszystkich kolumn (zgodnie z ich oczekiwaną kolejnością w wyniku)

# Zestaw 11 - flights-airports
## Etap *MapReduce*
93

| departure_airport_id   | status    |   flight_count |   avg_ticket_price |
|:-----------------------|:----------|---------------:|-------------------:|
| BIHN                   | Cancelled |            170 |            744.955 |

## Etap *Hive*
| continent   | country     |   total_flights |   avg_ticket_price |   rank_in_continent |
|:------------|:------------|----------------:|-------------------:|--------------------:|
| Africa      | Afghanistan |             489 |            774.662 |                  18 |


# Zestaw 12 - sales-products
## Etap *MapReduce*
800

| product_id                           | payment_type   |   total_quantity |   avg_unit_price |
|:-------------------------------------|:---------------|-----------------:|-----------------:|
| 017e16da-f0c0-48eb-99b8-a2bf7b731b8f | Card           |              312 |           250.18 |

## Etap *Hive*
8

| category   |   total_quantity |   avg_unit_price | brands_ranking                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|:-----------|-----------------:|-----------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Beauty     |            21401 |          254.427 | [{"brand":"Shanahan, Kling and Gerlach","rank_in_category":1},{"brand":"Howe LLC","rank_in_category":2},{"brand":"Torphy, Okuneva and Hamill","rank_in_category":3},{"brand":"Heller, Jerde and Oberbrunner","rank_in_category":4},{"brand":"Marvin, Hammes and Emmerich","rank_in_category":5},{"brand":"Collier, Weimann and Pfannerstill","rank_in_category":6},{"brand":"Vandervort, Runolfsdottir and Lakin","rank_in_category":7},{"brand":"Rowe, Lueilwitz and Hegmann","rank_in_category":8},{"brand":"Zieme, Farrell and Schaden","rank_in_category":8},{"brand":"Lindgren, D'Amore and Goyette","rank_in_category":10},{"brand":"Mosciski-Kling","rank_in_category":11},{"brand":"Lueilwitz, Cormier and Gottlieb","rank_in_category":12},{"brand":"Krajcik-Macejkovic","rank_in_category":13},{"brand":"Reinger-Hermiston","rank_in_category":14},{"brand":"Turner-O'Reilly","rank_in_category":15},{"brand":"Bauch Group","rank_in_category":16},{"brand":"Koelpin-Dare","rank_in_category":17}] |


# Zestaw 13 - football-matches
## Etap *MapReduce*
220

| team_id                              |   season |   matches_played |   avg_goals_per_match |
|:-------------------------------------|---------:|-----------------:|----------------------:|
| 0ec97648-1ab9-4f02-a000-6ad439697bbf |     2015 |              315 |               2.67937 |

## Etap *Hive*
5

| league     |   total_matches |   avg_goals_per_match | teams_ranking                                                                                                                                                                                                                                                                                                                                                   |
|:-----------|----------------:|----------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bundesliga |           25193 |               2.50022 | [{"team_id":"4c8c8a7f-58a3-46e3-8488-3a191d6e1e24","rank_in_league":1},{"team_id":"3dcfc466-56f9-4a21-b4ad-923d1a32cf1a","rank_in_league":2},{"team_id":"b6f94982-e51a-40e9-b2bb-7a4a6146b6a9","rank_in_league":3},{"team_id":"82d1432d-4fc9-4853-a4a0-4e52b5d5de4f","rank_in_league":4},{"team_id":"68bf322e-443a-4a96-a4ad-4c82251b1bcd","rank_in_league":5}] |


# Zestaw 14 - bus-trips
## Etap *MapReduce*
380

| operator_id                          |   departure_hour |   total_passengers |   avg_ticket_price |   wrong_avg |
|:-------------------------------------|-----------------:|-------------------:|-------------------:|------------:|
| 044847ae-eda3-4be0-b38f-5fbb4635bd37 |               04 |               4337 |            25.7293 |     26.4528 |

## Etap *Hive*
11

| region   | service_type   |   total_passengers |   avg_ticket_price |   rank_in_region |
|:---------|:---------------|-------------------:|-------------------:|-----------------:|
| Central  | Intercity      |              81049 |            27.3523 |                1 |


# Zestaw 15 - food-orders-restaurants
## Etap *MapReduce*
600

| restaurant_id                        | payment_type   |   orders_count |   avg_total_price |
|:-------------------------------------|:---------------|---------------:|------------------:|
| 000c40d9-805a-4493-8e8e-bcf4f603c5d2 | Card           |             72 |           85.1607 |

## Etap *Hive*
194

| country        | cuisine   |   total_orders |   avg_total_price |   rank_in_country |
|:---------------|:----------|---------------:|------------------:|------------------:|
| American Samoa | Italian   |            246 |           89.1304 |                 1 |


# Zestaw 16 - film-views
## Etap *MapReduce*
2000

| film_id   | platform   |   total_views |   avg_watch_time |
|:----------|:-----------|--------------:|-----------------:|
| FILM0001  | BingeNow   |            29 |          81.8483 |

## Etap *Hive*
245

| genre   | film_title         |   total_views |   pct_film_watch_time |   pct_genre_watch_time |
|:--------|:-------------------|--------------:|----------------------:|-----------------------:|
| Action  | A Farewell to Arms |            94 |              0.840458 |               0.611953 |


# Zestaw 17 - hospitals-visits
## Etap *MapReduce*
300

| hospital_id                          |   year |   total_patients |   avg_age |
|:-------------------------------------|-------:|-----------------:|----------:|
| 041798ae-9d7a-4948-b235-549575c6b7e1 |   2020 |               13 |   56.1538 |

## Etap *Hive*
50

| country   | hospital_type   |   total_patients |   avg_age |   rank_in_country |
|:----------|:----------------|-----------------:|----------:|------------------:|
| Angola    | Clinic          |              979 |   49.8856 |                 1 |


# Zestaw 18 - esports-heroes
## Etap *MapReduce*
29369

| player_id                            | hero_name   |   wins |   draws |   losses |
|:-------------------------------------|:------------|-------:|--------:|---------:|
| 01027715-f54e-49f8-9167-5b364bcd298c | Aatrox      |      2 |       2 |        1 |

## Etap *Hive*
3215

| region   | hero_name   |   total_wins |   total_draws |   total_losses |   avg_wins_for_hero |   above_avg_wins |
|:---------|:------------|-------------:|--------------:|---------------:|--------------------:|-----------------:|
| ASIA     | Aatrox      |           20 |            29 |             16 |                  15 |                1 |


# Zestaw 19 - stations-weather
## Etap *MapReduce*
32715

| station_id                           | date       |   avg_temp |   max_wind_speed |   no_measurements |
|:-------------------------------------|:-----------|-----------:|-----------------:|------------------:|
| 014efee3-d820-48e4-81a4-06b311fc315e | 2020-12-17 |    4.43333 |             78.5 |                 3 |

## Etap *Hive*
16238

| region       | date       |   region_day_avg_temp |   region_avg_temp |   avg_temp_deviation |
|:-------------|:-----------|----------------------:|------------------:|---------------------:|
| Dolnośląskie | 2020-12-17 |                  -2.5 |           6.69204 |             -9.19204 |


# Zestaw 20 - library-borrowings
## Etap *MapReduce*
2800

| book_id   |   borrow_year |   borrow_count |   avg_borrow_duration |   borrow_returned_count |
|:----------|--------------:|---------------:|----------------------:|------------------------:|
| BOOK00001 |          2021 |             16 |               41.1538 |                      13 |

## Etap *Hive*
60

| genre     |   borrow_year |   total_borrows |   avg_borrow_duration |   genre_year_share |
|:----------|--------------:|----------------:|----------------------:|-------------------:|
| Biography |          2020 |              91 |               32.9487 |            20.7289 |


# Zestaw 21 - parks-visits
## Etap *MapReduce*
27167

| park_id   | date       |   visits_count |   avg_group_size |
|:----------|:-----------|---------------:|-----------------:|
| PARK0001  | 2020-12-16 |              1 |                7 |

## Etap *Hive*
18

| nature_type   | region   |   total_visits |   avg_group_size |   avg_visits_for_type |   visits_deviation |
|:--------------|:---------|---------------:|-----------------:|----------------------:|-------------------:|
| Coast         | North    |           2580 |          3.97791 |                3799.5 |            -1219.5 |


# Zestaw 22 - shops-reviews
## Etap *MapReduce*
6097

| shop_id   | review_month   |   avg_rating |   review_count |
|:----------|:---------------|-------------:|---------------:|
| SHOP0001  | 2020-12        |          3.2 |              5 |

## Etap *Hive*
37

| region   | category   |   products_in_category |   region_category_avg_rating |   shop_count |
|:---------|:-----------|-----------------------:|-----------------------------:|-------------:|
| Central  | Books      |                     11 |                      3.02422 |            4 |


# Zestaw 23 - car-rentals
## Etap *MapReduce*
1181

| car_id   |   rental_year |   total_rentals |   completed_ratio |
|:---------|--------------:|----------------:|------------------:|
| CAR0001  |          2021 |              54 |          0.351852 |

## Etap *Hive*
60

| feature          |   rental_year |   feature_year_avg_rentals |   feature_year_avg_completed_ratio |   feature_avg_rentals_all_years |   above_avg_rentals |
|:-----------------|--------------:|---------------------------:|-----------------------------------:|--------------------------------:|--------------------:|
| Air Conditioning |          2020 |                    1.95161 |                           0.288978 |                         41.3501 |                   0 |



