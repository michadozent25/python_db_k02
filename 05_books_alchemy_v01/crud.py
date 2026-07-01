from models import Book
from sqlalchemy.orm import Session
from sqlalchemy import select
import json
from sqlalchemy.exc import SQLAlchemyError
import random


class BookRepository:
    def __init__(self,session:Session):
        self.session=session



    def save(self, book:Book) -> Book:
        
        self.session.add(book)
        self.session.commit()
        self.session.refresh(book) 
        return book
    def find_all(self)->list[Book]:
            return self.session.query(Book).all()
    
    def delete_by_id(self,id:int)->Book | None:
        book = self.session.get(Book,id)
        if book is not None:
            self.session.delete(book)
            self.session.commit()
        return book
    def find_by_genre(self, genre:str)-> list[Book]:
        stmt = select(Book).where(Book.genre.ilike(f"%{genre}%"))
        return list(self.session.scalars(stmt).all())
    
    def import_books(self,filename:str):
        with open(filename,encoding="utf-8") as file:
              data = json.load(file) 
        books =[
             Book(**book_data)  
             for book_data in data["books"] # books == json-root
        ]
        self.session.add_all(books)
        self.session.commit()

    def update(self, book: Book) -> Book | None:
        if book.id is None:
             return None
        updated_book = self.session.merge(book)
        self.session.commit()
        self.session.refresh(updated_book)
        return updated_book
    
    from sqlalchemy.exc import SQLAlchemyError

    def update2(self, book: Book) -> Book | None:
        if book.id is None:
            return None

        try:
            existing_book = self.session.get(Book, book.id)

            if existing_book is None:
                return None

            if book.title is not None:
                existing_book.title = book.title

            if book.author is not None:
                existing_book.author = book.author

            if book.genre is not None:
                existing_book.genre = book.genre

            if book.published_year is not None:
                existing_book.published_year = book.published_year

            self.session.commit()
            self.session.refresh(existing_book)

            return existing_book

        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Fehler beim Aktualisieren: {e}")
            return None

    def add_random_isbns(self) -> None:
        books = self.session.scalars(select(Book)).all()

        for book in books:
            book.isbn = str(random.randint(10**12, 10**13 - 1))

        self.session.commit()