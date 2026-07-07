from pydantic import BaseModel, EmailStr

class UserRead(BaseModel):
    id:int
    name:str
    email:EmailStr

class UserCreate(BaseModel):
    name:str
    email:EmailStr