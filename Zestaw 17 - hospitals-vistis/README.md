# Zestaw 17 – hospitals-visits

## Program MapReduce (2)

Działając na zbiorze `datasource1` `(1)` należy wyznaczyć podstawowe statystyki wizyt
pacjentów w poszczególnych szpitalach w kolejnych latach.

Dane powinny zostać pogrupowane według:  
* identyfikatora szpitala (`hospital_id`),  
* roku wizyty (`year`, wyodrębnionego z `date`).  

W ramach każdej grupy należy obliczyć:  
* `total_patients` – liczbę wizyt pacjentów w danej grupie,  
* `avg_age` – średni wiek pacjentów w danej grupie,  
* `female_count` – liczbę wizyt pacjentek (osób o płci `Female`) w danej grupie,  
* `unique_diseases` – listę unikalnych kodów chorób dla wszystkich wizyt w danej grupie.  

W wynikowym zbiorze `(3)` powinny znaleźć się następujące atrybuty:  
* `hospital_id` – identyfikator szpitala,  
* `year` – rok wizyty (`YYYY`),  
* `total_patients` – liczba wizyt pacjentów w danej grupie,  
* `avg_age` – średni wiek pacjentów w danej grupie,  
* `female_count` – liczba wizyt pacjentek o płci `Female` w danej grupie,  
* `unique_diseases` – listę unikalnych kodów chorób dla wszystkich wizyt w danej grupie.  

---

## Program Hive (5)

Działając na wyniku zadania MapReduce `(3)` oraz zbiorze danych `datasource4` `(4)` należy
powiązać statystyki dotyczące wizyt pacjentów z informacjami o szpitalach, a następnie obliczyć zestawienia
na poziomie krajów i typów szpitali.

Pole `unique_diseases` zawiera listę kodów chorób — należy je rozwinąć i na tej podstawie wyznaczyć
liczbę unikalnych kodów chorób odnotowanych w danej grupie (`unique_diseases_count`).

Dla każdego kraju i typu szpitala należy obliczyć:  
* łączną liczbę pacjentów obsłużonych w kraju w ramach danego typu szpitala,  
* średni wiek pacjentów,  
* łączną liczbę wizyt pacjentek o płci `Female`,  
* liczbę unikalnych kodów chorób odnotowanych w danej grupie,  
* odchylenie liczby pacjentów w danym kraju i typie szpitala od średniej liczby pacjentów
  dla tego samego typu szpitala we wszystkich krajach (`patients_deviation`).  

Wynik `(6)` powinien zawierać następujące atrybuty:  
* `country` – kraj,  
* `hospital_type` – typ szpitala (np. *General*, *Specialist*, *Clinic*),  
* `total_patients` – łączna liczba pacjentów w kraju dla danego typu szpitala,  
* `avg_age` – średni wiek pacjentów,  
* `female_count` – łączna liczba wizyt pacjentek o płci `Female`,  
* `unique_diseases_count` – liczba unikalnych kodów chorób odnotowanych w danej grupie,  
* `patients_deviation` – różnica między liczbą pacjentów w danym kraju i typie szpitala
  a średnią liczbą pacjentów dla tego samego typu szpitala we wszystkich krajach.  

---

Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu
– patrz opis projektu na stronie kursu.