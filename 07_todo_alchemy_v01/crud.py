from models import Todo,User
from sqlalchemy.orm import Session
from sqlalchemy import text,select

class TodoRepository():
    def __init__(self, session:Session):
        self.session=session

    
    def save(self, todo:Todo) -> Todo:
        self.session.add(todo)
        self.session.commit()
        self.session.refresh(todo) 
        return todo