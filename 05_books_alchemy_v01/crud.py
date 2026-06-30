from models import Book
from sqlalchemy.orm import Session
from sqlalchemy import select


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