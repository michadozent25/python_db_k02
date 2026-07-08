# RestService
from models import User, Todo
from database import  get_db
from schema import *
from crud import UserRepository, TodoRepository
from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.orm import Session


user_router= APIRouter(prefix="/users")
todo_router= APIRouter(prefix="/todo")

@user_router.post("/",response_model=UserRead)
def create_user(user_create:UserCreate, db:Session =Depends(get_db)):
    repo = UserRepository(db)
    new_user = User(username=user_create.username,
                    password=user_create.password)
    return repo.create(new_user)