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
    t2 = Todo(task="einkaufen",description="Brot")
    t3 = Todo(task="lesen",description="schönes Buch")



    print(todo_repo.new_todo_by_user(u1.id,t1))
    print(todo_repo.new_todo_by_user(u1.id,t2))
    print(todo_repo.new_todo_by_user(u1.id,t3))

    todo_repo.update_todo_state(t1.id,"DONE")

    print(todo_repo.find_todo_by_user(u1.id))

   
if __name__=="__main__":
    main()