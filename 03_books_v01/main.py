from models import Book
from crud import BookRepository
from db_connect import connect_db
from csv_reader import load_csv

def main():
    conn = connect_db()
    repo =  BookRepository(conn)
    # repo.save( Book(title="Schönes Kochbuch",author="Maxe", genre="Sachbuch",published_year=2000))
    
    book_list = load_csv('books.csv')
    print(book_list)

    #repo.save_books(book_list)

if __name__=="__main__":
    main()