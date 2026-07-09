# RestService
from models import User, Todo
from database import  get_db
from schema import *
from crud import UserRepository, TodoRepository
from fastapi import FastAPI, Depends, APIRouter, HTTPException
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

# Aufgabe : Test in Swagger
@user_router.get("/{user_id}/todos",response_model=list[TodoRead])# http:/localhost:8000/users/1/todos
def get_all_todos_by_userid(user_id,db:Session =Depends(get_db)):
    repo = TodoRepository(db)
    return repo.find_todo_by_user(user_id)

@user_router.get("/",response_model=list[UserRead])#http:/localhost:8000/users/
def get_all_users(db:Session =Depends(get_db)):
    repo = UserRepository(db)
    return repo.find_all()


@todo_router.get("/{user_id}/todos/open",response_model=list[TodoRead])
def get_all_open_todos_by_userid(user_id:int,db:Session =Depends(get_db)):
    repo = TodoRepository(db)
    return repo.find_open_todos_by_user(user_id)

@user_router.post("/authenticate",response_model=UserRead)
def authenticate_user(user_login:UserLogin,db:Session =Depends(get_db)):
    repo = UserRepository(db)
    user = repo.find_user_by_credentials(user_login.username, user_login.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid Username or Password!")

    return user