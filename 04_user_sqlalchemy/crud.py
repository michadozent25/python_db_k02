from models import User
from sqlalchemy.orm import Session
from sqlalchemy import text,select

class UserRepository:

    def __init__(self, session:Session):
        self.session=session

    def save(self, user:User) -> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user) # Userobjekt aktualisieren
        return user
    
    def find_all(self)->list[User]:
        return self.session.query(User).all()
    
    def find_by_id(self,id:int)-> User:
        return self.session.query(User).filter(User.id ==id).first()
    
    def delete_by_id(self,id:int)->User | None:
        user = self.session.get(User,id)
        if user is not None:
            self.session.delete(user)
            self.session.commit()
        return user
    
    def find_user_by_name(self, name:str)->list[User]:
        stmt = text("select * from user where name like :name" )# SQL-Schreibweise
        return self.session.execute(stmt,{"name":f"%{name}%"} )


    def find_user_by_name2(self,name:str)->list[User]:
        stmt =  select(User).where(User.name.ilike(f"%{name}%"))
        return self.session.execute(stmt).scalars().all()

    
