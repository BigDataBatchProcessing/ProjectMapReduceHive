# Zestaw 17 – hospitals-visits

## Program MapReduce (2)

Działając na zbiorze `datasource1` `(1)` należy wyznaczyć podstawowe statystyki wizyt pacjentów w poszczególnych szpitalach.  

Dane powinny zostać pogrupowane według:  
* identyfikatora szpitala (`hospital_id`),  
* roku wizyty (`year`).  

W ramach każdej grupy należy obliczyć dwie miary:  
* `total_patients` – liczba wizyt pacjentów w danym roku i szpitalu,  
* `avg_age` – średni wiek pacjentów w danym roku i szpitalu.  

W wynikowym zbiorze `(3)` powinny znaleźć się cztery atrybuty:  
* `hospital_id` – identyfikator szpitala,  
* `year` – rok wizyty (`YYYY`),  
* `total_patients` – liczba wizyt pacjentów w danej grupie,  
* `avg_age` – średni wiek pacjentów w danej grupie.  

---

## Program Hive (5)

Działając na wyniku zadania MapReduce `(3)` oraz zbiorze danych `datasource4` `(4)` należy powiązać wizyty pacjentów z informacjami o szpitalach.  

Na podstawie tych danych należy wyliczyć zestawienia na poziomie krajów i typów szpitali.  

Dla każdego kraju i typu szpitala należy obliczyć:  
* łączną liczbę pacjentów obsłużonych w kraju w ramach danego typu szpitala,  
* średni wiek pacjentów obsłużonych w kraju w ramach danego typu szpitala.    

Dodatkowo – w ramach każdego kraju – należy określić ranking typów szpitali według liczby obsłużonych pacjentów.  

Wynik `(6)` powinien zawierać następujące atrybuty:  
* `country` – kraj,  
* `hospital_type` – typ szpitala (np. *General*, *Specialist*, *Clinic*),  
* `total_patients` – łączna liczba pacjentów w kraju dla danego typu szpitala,  
* `avg_age` – średni wiek pacjentów,  
* `rank_in_country` – pozycja typu szpitala w rankingu liczby obsłużonych pacjentów w ramach danego kraju.  

---

Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu – patrz opis projektu na stronie kursu.
