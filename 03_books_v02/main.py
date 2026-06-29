from models import Book
from crud import BookRepository
from db_connect import connect_db
from csv_reader import load_csv
from db_schema import create_new_books_table

def main():
    ############## Test Setup ###################
    conn = connect_db()
    create_new_books_table(conn)
    repo =  BookRepository(conn)
    #repo.save( Book(title="Schönes Kochbuch",author="Maxe", genre="Sachbuch",published_year=2000))
    
    book_list = load_csv('books.csv')
    #print(book_list)

    repo.save_books(book_list)

    #########################################
    # all_books = repo.find_all()
    # print(all_books) 

    print("Deleted: ",repo.delete_by_id(1))

if __name__=="__main__":
    main()