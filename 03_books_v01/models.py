from dataclasses import dataclass

@dataclass
class Book:
    id:int | None = None # lesen:mit id, schreiben ohne id (autoincrement)
    title:str =""
    author:str = ""
    genre:str =""
    published_year:int =0