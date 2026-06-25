class Person:
    '''
    Model-Klasse (Datenklasse)
    '''


    ''' Konstruktor
        Aufruf: Person(3,"Max","max@web.de") 
    '''
    def __init__(self, id:int, name:str, email: str ):
        self._id = id
        self._name = name
        self._email = email
    def __repr__(self): #toString
        return f"Person(id={self._id} , name={self._name})"
    

    @property # lesen
    def id(self)->int:
        return self._id
    
    @id.setter # 
    def id(self,id):
        self._id = id


    @property 
    def name(self)->str:
        return self._name
    
    @name.setter  
    def name(self,name):
        self._name = name

# Variante 2 für Model/Datenklassen

from dataclasses import dataclass

@dataclass
class Kurs:
    id:int
    name:str
    doz:str =""
    wochen: int=4 