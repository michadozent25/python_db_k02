from database import Base, engine, session
from models import User, Todo
from crud import UserRepository,TodoRepository

def main():
    Base.metadata.drop_all(engine)# delete all Tables
    Base.metadata.create_all(engine) # create Tables if not exists


    user_repo= UserRepository(session)
    todo_repo = TodoRepository(session)

    u1 = User(username="max",password="123")
    create_user = user_repo.create(u1)


    logged_in = user_repo.find_user_by_credentials("max","123")

    if logged_in is not None:
        print("Login erfolgreich!", logged_in)


    logged_in2 = user_repo.find_user_by_credentials("max","1111")

    if logged_in is  None:
        print("Login nicht erfolgreich!", logged_in2)

   
if __name__=="__main__":
    main()