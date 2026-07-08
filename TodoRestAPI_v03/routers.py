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

@todo_router.post("/",response_model=TodoRead) # oder user_id im Pfad "/{user_id}/todos"
def create_todo_by_userid(user_id:int,todo_create:TodoCreate, db:Session =Depends(get_db)):
    repo = TodoRepository(db)
    new_todo = Todo(**todo_create.model_dump())

    return repo.new_todo_by_user(user_id,new_todo)

# Aufgabe 
@todo_router.get(...)
def get_all_todos_by_userid(...):
    pass

@user_router.get(...)
def get_all_users(...):
    pass


@todo_router.get(...)
def get_all_open_todos_by_userid(...):
    pass