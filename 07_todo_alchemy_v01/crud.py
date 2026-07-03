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
    

    def update_todo_state(self, todo_id:int, new_state:str)->Todo | None:
        # TODO check new_state
        allowed = {"OPEN","IN_PROGRESS","DONE"}
        if new_state not in allowed:
            raise ValueError(f"Invalid State, allowed: {allowed}")


        todo = self.session.get(Todo,todo_id)
        if not todo:
            return None
        todo.state = new_state
        self.session.commit()
        self.session.refresh(todo)
        return todo



    def find_todos_by_task(self,user_id:int,task:str)->list[Todo]:
        return (
            self.session.query(Todo)
            .filter(
                Todo.user_id==user_id, 
                Todo.task.ilike(f"%{task}%")
            )
            .all()
        )


    

class UserRepository():
    def __init__(self, session:Session):
        self.session=session
    def create(self, user:User) -> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user) 
        return user
