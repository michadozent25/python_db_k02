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
    
class Todo(Base, BaseRepr):
     __tablename__="todos"
     id= Column(Integer,primary_key=True)
     task=Column(String(150),nullable=False)
     description=Column(Text)
     deadline=Column(Date)
     state=Column(Enum("OPEM","IN_PRGRESS","DONE"), nullable=False, default="OPEN")

class User(Base,BaseRepr):
    pass
