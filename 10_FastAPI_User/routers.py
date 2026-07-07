# RestService
from models import User
from database import  get_db
from schema import UserRead,UserCreate
from crud import UserRepository
from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.orm import Session

user_router = APIRouter()


@user_router.get("/users/", response_model=list[UserRead])
def get_all_users(db:Session = Depends(get_db)):
    repo = UserRepository(db)
    return repo.find_all()

@user_router.post("/users/", response_model=UserRead)
def create_user(user_create:UserCreate, db:Session = Depends(get_db)):

    repo = UserRepository(db)
    new_user= User(**user_create.model_dump())# konverieren UserCreate to User (DB)

    return repo.save(new_user)
