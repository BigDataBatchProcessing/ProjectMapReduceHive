# Oczekiwane wyniki dla danych testowych 2025-01

Poniżej zamieszczone zostały oczekiwane wyniki dla zestawów danych `2025-01` dla poszczególnych ze zestawów projektów. 

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
300

| departure_airport_id | status    | flight_count | avg_ticket_price |
|----------------------|-----------|--------------|------------------|
| CAP3                 | Cancelled | 156          | 754.85859        |


## Etap *Hive*
97

| continent | country | total_flights | avg_ticket_price | rank_in_continent |
|-----------|---------|----------------|-------------------|--------------------|
| Africa    | Bahrain | 501            | 755.442511        | 8                  |


# Zestaw 12 - sales-products
## Etap *MapReduce*

800

| product_id                             | payment_type | total_quantity | avg_unit_price |
|-----------------------------------------|--------------|----------------|----------------|
| 00d92b75-1195-4f9f-9ff1-030bfa493c0c    | Card         | 307            | 3.916467       |

## Etap *Hive*

8

| category | total_quantity | avg_unit_price | brands_ranking |
|----------|----------------|----------------|----------------|
| Beauty   | 37384          | 4.127351       | [{"brand":"Schmeler, Lang and Schroeder","rank_in_category":1},{"brand":"Hand, Rowe and Ledner","rank_in_category":2},{"brand":"Schowalter, Hyatt and Beahan","rank_in_category":3},{"brand":"Kautzer Group","rank_in_category":4},{"brand":"Langosh, Moen and Wilderman","rank_in_category":5},{"brand":"Mitchell, Hermiston and Konopelski","rank_in_category":6},{"brand":"O'Conner Group","rank_in_category":7},{"brand":"Ledner-Kilback","rank_in_category":8},{"brand":"Hyatt-Kutch","rank_in_category":9},{"brand":"Yundt, Dach and Robel","rank_in_category":10},{"brand":"Ankunding, Schinner and Keeling","rank_in_category":11},{"brand":"Hilpert-Lind","rank_in_category":12},{"brand":"Schinner-Blick","rank_in_category":12},{"brand":"Kutch and Sons","rank_in_category":14},{"brand":"Mohr LLC","rank_in_category":15},{"brand":"Ruecker Group","rank_in_category":16},{"brand":"Mann, Bashirian and Green","rank_in_category":17},{"brand":"Williamson-Kiehn","rank_in_category":18},{"brand":"Pouros-Wilkinson","rank_in_category":19},{"brand":"Crooks LLC","rank_in_category":20},{"brand":"Kuphal and Sons","rank_in_category":21},{"brand":"Torp, Robel and Rath","rank_in_category":22},{"brand":"Koss, Schuppe and Armstrong","rank_in_category":23},{"brand":"Price-Bergnaum","rank_in_category":23},{"brand":"Murazik Inc","rank_in_category":25},{"brand":"Hickle Inc","rank_in_category":26},{"brand":"Conn-Kris","rank_in_category":27},{"brand":"Steuber-Koss","rank_in_category":28},{"brand":"Walter-Jones","rank_in_category":29},{"brand":"Parisian-Russel","rank_in_category":30}] |


# Zestaw 13 - football-matches
## Etap *MapReduce*
220

| team_id                               | season | matches_played | avg_goals_per_match |
|---------------------------------------|--------|-----------------|----------------------|
| 0004a1c0-e1fd-4cae-8890-235c93449abc  | 2015   | 337             | 2.531157            |

## Etap *Hive*

5

| league     | total_matches | avg_goals_per_match | teams_ranking |
|------------|----------------|----------------------|----------------|
| Bundesliga | 29993          | 2.489281            | [{"team_id":"4d7632f9-9f2c-40ea-a8ce-afd8d7792abd","rank_in_league":1},{"team_id":"e3f5aeb0-c499-4948-9019-dd7de0060bb9","rank_in_league":2},{"team_id":"69ec09b0-8fcf-4e38-8ab6-a60c751bdc49","rank_in_league":3},{"team_id":"575fae5f-57e2-47ec-b651-7fd27066eb86","rank_in_league":4},{"team_id":"305b2ef4-3023-4179-8a7b-53a5aa05958c","rank_in_league":5},{"team_id":"143b9bc7-cdb7-46f2-af70-c7cffc9c7162","rank_in_league":6}] |


# Zestaw 14 - bus-trips
## Etap *MapReduce*

380

| operator_id                             | departure_hour | total_passengers | avg_ticket_price | wrong_avg   |
|-----------------------------------------|----------------|-----------------|-----------------|-------------|
| 05b88b9d-b2df-4864-899b-c47411101f0a    | 04             | 3296            | 27.678574       | 27.725094   |


## Etap *Hive*
11

| region  | service_type | total_passengers | avg_ticket_price | rank_in_region |
|---------|--------------|-----------------|-----------------|----------------|
| Central | Express      | 78651           | 27.422577       | 2              |


# Zestaw 15 - food-orders-restaurants
## Etap *MapReduce*

600

| restaurant_id                           | payment_type | orders_count | avg_total_price |
|-----------------------------------------|--------------|--------------|----------------|
| 000f9c8f-2fc7-4346-844d-c04f10751265    | Card         | 77           | 86.349091      |


## Etap *Hive*

195

| country | cuisine | total_orders | avg_total_price | rank_in_country |
|---------|---------|--------------|----------------|----------------|
| Algeria | Chinese | 264          | 82.108295      | 1              |

> Uwagi
> * istnieje teoria, że liczba wierszy powinna być 194 - nie potwierdzam

# Zestaw 16 - film-views
## Etap *MapReduce*

2000

| film_id  | platform  | total_views | avg_watch_time |
|----------|-----------|-------------|----------------|
| FILM0001 | BingeNow | 25          | 71.428667      |


## Etap *Hive*

245

| genre  | film_title                  | total_views | pct_film_watch_time | pct_genre_watch_time |
|--------|-----------------------------|-------------|--------------------|--------------------|
| Action | A Many-Splendoured Thing    | 102         | 0.773885           | 0.606998
           |


# Zestaw 17 - hospitals-vistis
## Etap *MapReduce*

300

| hospital_id                           | year | total_patients | avg_age   |
|---------------------------------------|------|----------------|-----------|
| 0cd858b2-a0fb-4574-a017-667d5b7def43 | 2020 | 26             | 57.538462 |


## Etap *Hive*

45

| country                                      | hospital_type | total_patients | avg_age    | rank_in_country |
|----------------------------------------------|---------------|----------------|------------|----------------|
| Antarctica (the territory South of 60 deg S) | Clinic        | 979            | 49.390194  | 1              |



# Zestaw 18 - esports-heroes
## Etap *MapReduce*

56369

| player_id                             | hero_name | wins | draws | losses |
|---------------------------------------|-----------|------|-------|--------|
| 072b5fae-748c-4cbc-a287-ea97cb6a7097  | A-Bomb    | 0    | 1     | 0      |


## Etap *Hive*

25423

| region | hero_name | total_wins | total_draws | total_losses | avg_wins_for_hero | above_avg_wins |
|--------|-----------|------------|-------------|--------------|------------------|----------------|
| ASIA   | A-Bomb    | 1          | 0           | 0            | 1.000000         | 0              |


# Zestaw 19 - stations-weather
## Etap *MapReduce*

32876

| station_id                             | date       | avg_temp | max_wind_speed |
|----------------------------------------|------------|----------|----------------|
| 112ec819-5b76-4e8c-9a6f-e17fafbf07e9   | 2020-11-14 | 37.6     | 16.5           |


## Etap *Hive*

16238

| region         | date       | region_day_avg_temp | region_avg_temp | avg_temp_deviation |
|----------------|------------|-------------------|----------------|------------------|
| Dolnośląskie   | 2020-11-13 | 15.05             | 6.239733       | 8.810267         |


# Zestaw 20 - library-borrowings
## Etap *MapReduce*

2969

| book_id   | borrow_year | borrow_count | avg_borrow_duration | borrow_returned_count |
|-----------|-------------|--------------|-------------------|----------------------|
| BOOK00001 | 2020        | 2            | 16.0              | 1                    |


## Etap *Hive*

60

| genre     | borrow_year | total_borrows | avg_borrow_duration | genre_year_share |
|-----------|-------------|---------------|-------------------|-----------------|
| Biography | 2020        | 288           | 33.055118         | 21.021898       |


# Zestaw 21 - parks-visits
## Etap *MapReduce*

27353

| park_id  | date       | visits_count | avg_group_size |
|----------|------------|--------------|----------------|
| PARK0001 | 2020-11-11 | 1            | 4.0            |


## Etap *Hive*

22

| nature_type | region  | total_visits | avg_group_size | avg_visits_for_type | visits_deviation |
|-------------|---------|--------------|----------------|-------------------|-----------------|
| Coast       | Central | 2513         | 3.968823       | 2505.0            | 8.0             |


# Zestaw 22 - shops-reviews
## Etap *MapReduce*

6087

| shop_id  | review_month | avg_rating | review_count |
|----------|--------------|------------|--------------|
| SHOP0001 | 2020-11      | 2.75       | 4            |


## Etap *Hive*

36

| region  | category | products_in_category | region_category_avg_rating | shop_count |
|---------|----------|--------------------|---------------------------|------------|
| Central | Books    | 7                  | 3.002081                  | 2          |


# Zestaw 23 - car-rentals
## Etap *MapReduce*
1200

| car_id  | rental_year | total_rentals | completed_ratio |
|---------|-------------|---------------|----------------|
| CAR0001 | 2020        | 10            | 0.5            |


## Etap *Hive*

60

| feature           | rental_year | feature_year_avg_rentals | feature_year_avg_completed_ratio | feature_avg_rentals_all_years | above_avg_rentals |
|------------------|-------------|-------------------------|---------------------------------|-------------------------------|------------------|
| Air Conditioning | 2020        | 7.064516                | 0.351518                        | 42.08871                      | 0                |

