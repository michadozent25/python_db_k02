from database import Base, engine, session
from models import User
from crud import UserRepository

def main():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine) # create if not exists

    repo = UserRepository(session)
    repo.save(User(name="otto",email="otti@web.de") )

    del_user = repo.delete_by_id(1)
    print(del_user)


if __name__=="__main__":
    main()