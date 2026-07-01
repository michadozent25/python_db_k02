from database import Base
from sqlalchemy import Column, Integer, String

class Book(Base):
    __tablename__ ="book"
    id = Column(Integer,primary_key=True)# default auto_increment
    title = Column(String(100),nullable=False)
    genre = Column(String(50),nullable=False)
    author = Column(String(50),nullable=False)
    published_year = Column(Integer,nullable=False) 
    isbn = Column(String(20),nullable=False)

    def __repr__(self):
        return f"Book(id={self.id}, title={self.title}, genre={self.genre}, author={self.author}, published_year={self.published_year})"