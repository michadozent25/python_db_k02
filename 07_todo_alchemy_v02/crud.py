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

    def find_open_todos_by_user(self,user_id:int)->list[Todo]:
        return (
            self.session.query(Todo)
            .filter(
                Todo.user_id == user_id,
                Todo.state == "OPEN"
            )
            .all()

        )
    
    def delete_todo(self, todo_id:int)-> Todo | None:
        """ """
        todo = self.session.get(Todo,todo_id)
        if todo is  None:
            return None
  
        self.session.delete(todo)
        self.session.commit()
        return todo


    def delete_all_done_todos(self,user_id:int)->int:
        todos = (
            self.session.query(Todo)
            .filter(
                Todo.user_id == user_id,
                Todo.state == "DONE"
            )
            .all()
        )
        count = len(todos)
        for todo in todos:
            self.session.delete(todo)
        self.session.commit()
        return  count

class UserRepository():
    def __init__(self, session:Session):
        self.session=session
    def create(self, user:User) -> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user) 
        return user
    
    def delete_user(self, user_id:int)-> User | None:
        user = self.session.get(User, user_id)
        if user is None:
            return None
        self.session.delete(user)
        self.session.commit()
        return user

    def find_user_by_id(self, user_id:int)-> User | None:
        return self.session.get(User, user_id)
    
    def find_user_by_credentials(self, username:str, password:str)->User |None:
        """ 
        Nötig für einen späteren Login-Vorgang
        - User aus DB holen
        - Passwort check (util.py:verify_password)  
        - User oder None zurückgeben
        """
