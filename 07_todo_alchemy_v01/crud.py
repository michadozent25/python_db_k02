from models import Todo,User
from sqlalchemy.orm import Session
from sqlalchemy import text,select

class TodoRepository():
    def __init__(self, session:Session):
        self.session=session

    
    # def save(self, todo:Todo) -> Todo:
    #     self.session.add(todo)
    #     self.session.commit()
    #     self.session.refresh(todo) 
    #     return todo
    def new_todo_by_user(self,  user_id:int, todo:Todo)->Todo:
        user = self.session.get(User,user_id)
        user.todos.append(todo)
        self.session.commit()
        self.session.refresh(todo)
        return todo
    def find_todo_by_user(self,user_id:int)->list[Todo]:
        return self.session.query(Todo).filter(Todo.user_id==user_id).all()


    

class UserRepository():
    def __init__(self, session:Session):
        self.session=session
    def create(self, user:User) -> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user) 
        return user
