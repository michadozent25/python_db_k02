import csv
import os
from models import Book

def load_csv(filename:str)->list[Book]:
    #Umgang mit relativen Pfaden (Workaround)
    script_dir = os.path.dirname(__file__)
    full_path = os.path.join(script_dir,filename)

    book_list = []

    with open(full_path,newline='', encoding='utf-8') as csvfile:
        reader  = csv.DictReader(csvfile)
        for row in reader:
   
           # Book-Objekte erzeugen
           # Books zur book_list hinzufügen 
           book_list.append(Book( ... ))
    return book_list

#print(load_csv('users.csv'))