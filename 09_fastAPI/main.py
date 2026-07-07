from fastapi import FastAPI
from pydantic import BaseModel

# start: uvicorn main:app --reload
app = FastAPI()

class Item(BaseModel):
    name:str
    price:float


@app.get("/")
def get_root():
    return { "message":"Hallo Rest"}

# @app.get("/items/{item_id}")
# def get_item(item_id:int):
#     return {"id":item_id}

@app.get("/items/{item_id}")# http://localhost:8000/items/42?q=Hallo
def get_item2(item_id:int, q:str):
    return {"id":item_id, "name":q}

@app.post("/items") # nicht im Browser Testbar! hier http://localhost:8000/docs
def create_item(item:Item):
    return {"message":"Item erzeugt","item":item}