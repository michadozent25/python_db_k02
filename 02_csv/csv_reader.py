import csv
import os

def load_csv(filename:str):
    #Umgang mit relativen Pfaden (Workaround)
    script_dir = os.path.dirname(__file__)
    full_path = os.path.join(script_dir,filename)

    users = []

    with open(full_path,newline='', encoding='utf-8') as csvfile:
        reader  = csv.DictReader(csvfile)
        for row in reader:
            users.append((row['name'], row['email']))
    return users

#print(load_csv('users.csv'))