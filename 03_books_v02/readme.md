# Books-DB
## Version 02

## Feature

* save(Book)
* save_books(Book-List)
* read csv
## Feature Todo
* find_all -> list[Book] 
* find_by_title
* find_by_genre
* delete_by_id(id)
* update(Book)
## Struktur

* models:Book
* crud:BookRepository
* service:csv
* database: connect, schema
* main: Test Feature
## Resources
* books.csv
## Aufgabe

* implementiere die folgenden crud-Methoden im BookRepository
  * find_all(self)->list[Book]
  * delete_by_id(id) - soll einen Datensatz nach id löschen
### Zusatz
* find_by_title(title)
* find_by_genre(author)