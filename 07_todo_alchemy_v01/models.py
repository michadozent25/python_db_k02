from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey,Text,Date,Enum
from sqlalchemy.orm import relationship

class BaseRepr:
    """ generischhe __repr__Methode
        alle Klassen, die von  BaseRepr erben, bekommen automatisch eine
        def __repr__-Methode
    """
    def __repr__(self):
        fields = ", ".join(
            f"{col.name}={getattr(self, col.name)!r}"
            for col in self.__table__.columns
        )
        return f"<{self.__class__.__name__}({fields})>"
 # N   
class Todo(Base, BaseRepr):
     __tablename__="todos"
     id= Column(Integer,primary_key=True)
     task=Column(String(150),nullable=False)
     description=Column(Text)
     deadline=Column(Date)
     state=Column(Enum("OPEN","IN_PROGRESS","DONE"), nullable=False, default="OPEN")
     user_id=Column(Integer, ForeignKey("user.id"),nullable=False)
     user=relationship("User",back_populates="todos")
# 1
class User(Base,BaseRepr):
    __tablename__="user"
    id=Column(Integer, primary_key=True)
    username = Column(String(20),nullable=False,unique=True)
    password=Column(String(100))
    todos=relationship("Todo",back_populates="user",cascade="all, delete-orphan")
