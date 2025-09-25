# Zestaw 20 - library-borrowings

## Program MapReduce (2)

Działając na zbiorze `datasource1` `(1)` należy obliczyć statystyki wypożyczeń książek.  

Dane powinny zostać pogrupowane według:  
* identyfikatora książki (`book_id`),  
* roku wypożyczenia (`borrow_year`, wyodrębnionego z `borrow_date`).  

W ramach każdej grupy należy obliczyć:  
* `borrow_count` – liczbę wypożyczeń książki w danym roku,  
* `avg_borrow_duration` – średni czas trwania wypożyczenia (w dniach, tylko dla rekordów ze statusem `RETURNED`).  

Wynikowy zbiór `(3)` powinien zawierać następujące atrybuty:  
* `book_id` – identyfikator książki,  
* `borrow_year` – rok wypożyczenia,  
* `borrow_count` – liczba wypożyczeń książki w danym roku,  
* `avg_borrow_duration` – średni czas trwania wypożyczenia książki w danym roku.  

---

## Program Hive (5)

Działając na wyniku zadania MapReduce `(3)` oraz zbiorze danych `datasource4` `(4)` należy powiązać informacje o wypożyczeniach z opisami książek.  

Na podstawie tych danych należy wyliczyć, dla każdego gatunku książek (`genre`) i roku (`borrow_year`):  
* łączną liczbę wypożyczeń (`total_borrows`),  
* średnią długość wypożyczenia (`avg_borrow_duration`),  
* udział procentowy liczby wypożyczeń książek w danym gatunku w danym roku względem wszystkich wypożyczeń w danym roku (`genre_year_share`).  

Wynik `(6)` powinien zawierać następujące atrybuty:  
* `genre` – gatunek literacki,  
* `borrow_year` – rok wypożyczenia,  
* `total_borrows` – łączna liczba wypożyczeń książek w danym gatunku i roku,  
* `avg_borrow_duration` – średni czas trwania wypożyczeń w danym gatunku i roku,  
* `genre_year_share` – udział procentowy liczby wypożyczeń książek z danego gatunku w danym roku względem wszystkich wypożyczeń w danym roku.  

---

Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu – patrz opis projektu na stronie kursu.  
