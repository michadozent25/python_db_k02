from database import Base, engine, session
from models import User, Todo
from crud import UserRepository,TodoRepository

def main():
    Base.metadata.drop_all(engine)# delete all Tables
    Base.metadata.create_all(engine) # create Tables if not exists


    user_repo= UserRepository(session)
    todo_repo = TodoRepository(session)

    u1 = User(username="max",password="123")
    user_repo.create(u1)

    t1 = Todo(task="sport",description="schwimmen")

    print(todo_repo.new_todo_by_user(u1.id,t1))

   
if __name__=="__main__":
    main()