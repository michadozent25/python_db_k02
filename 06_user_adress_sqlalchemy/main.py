from database import Base, engine, session
from models import User, Address
from crud import UserRepository

def main():
    Base.metadata.drop_all(engine)# delete all Tables
    Base.metadata.create_all(engine) # create Tables if not exists

    repo = UserRepository(session)
    address1 = Address(postal_code="12034",street="Dorfstr. 3",city="Berlin" )

    u1 =User(name="otto",email="otti@web.de")
    u1.addresses.append(address1)

    repo.save(u1 )

    print(repo.find_all())

    # del_user = repo.delete_by_id(1)
    # print(del_user)


if __name__=="__main__":
    main()