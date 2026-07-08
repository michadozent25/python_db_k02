from pydantic import BaseModel, EmailStr, Field

class UserRead(BaseModel):
    id:int
    name:str
    email:EmailStr

class UserCreate(BaseModel):
    name:str = Field(min_length=2, max_length=20)
    email:EmailStr