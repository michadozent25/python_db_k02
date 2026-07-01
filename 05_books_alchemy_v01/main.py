from database import Base, engine, session
from models import Book
from crud import BookRepository



def main():

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine) # create if not exists
    repo = BookRepository(session)
    # repo.save(Book(title="Schönes Kochbuch",author="Maxe", genre="Sachbuch",published_year=2000))
    #print(repo.save(Book(title="Kochbuch2",author="Otto", genre="Sachbuch",published_year=2009)))
    repo.import_books("json/books.json")

    repo.add_random_isbns()
    

    # all_books = repo.find_all()
    # for book in all_books:
    #     print(book)

    # print("find by genre: ",repo.find_by_genre("Sachbuch"))
    # del_book = repo.delete_by_id(1)
    # print("delete:", del_book)

    #print(repo.update( Book(id=1, title="Schönes neues Kochbuch")))

 

if __name__ == "__main__":

    main()