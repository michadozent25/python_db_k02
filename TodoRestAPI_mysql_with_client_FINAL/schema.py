from pydantic import BaseModel, Field
from datetime import date
from enum import Enum

#------------------------ User ----------------

class UserBase(BaseModel):
    username:str

class  UserCreate(UserBase):
    password: str=Field(min_length=5,max_length=20)#TODO Welche Zeichen? -Pattern:regex

class UserRead(UserBase):
    id:int
    todos:list[TodoRead] = []

#--------------------------Todo----------------
class TodoState(str,Enum):
    OPEN="OPEN"
    IN_PROGRESS="IN_PROGRESS"
    DONE="DONE"

class TodoBase(BaseModel):
    task:str 
    description:str | None = None
    deadline:date | None = None
    state:TodoState = TodoState.OPEN
    # FIXME user_id ?

class TodoCreate(TodoBase):
    pass

class TodoRead(TodoBase):
    id:int
    user_id:int

class UserLogin(BaseModel):
    username:str
    password:str