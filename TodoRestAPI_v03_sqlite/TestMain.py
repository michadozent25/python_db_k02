from database import Base, engine, session
from models import User, Todo
from crud import UserRepository,TodoRepository


def main():
    Base.metadata.drop_all(engine)# delete all Tables
    Base.metadata.create_all(engine) # create Tables if not exists


    user_repo= UserRepository(session)
    todo_repo = TodoRepository(session)

    
  
if __name__=="__main__":
    main()