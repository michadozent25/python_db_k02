from db_connect import connect_db
from csv_reader import load_csv

try:
    conn = connect_db()
    # daten =[
    #     ("Arno","arno@web.de"),
    #     ("Ina","ina@web.de"),
    #     ("Otto","otto@web.de")
    # ]
    daten = load_csv('users.csv')
    sql= "INSERT INTO users (name,email) VALUES (%s,%s)"
    cursor = conn.cursor()
    cursor.executemany(sql,daten)
    conn.commit()
except Exception as e:
    print(e)