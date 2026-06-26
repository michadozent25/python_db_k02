from models import Book
from mysql.connector import MySQLConnection
class BookRepository:
    def __init__(self,conn:MySQLConnection):
        self.conn=conn


    def save(self, book:Book):
        '''  '''
        try:
            cursor = self.conn.cursor()
            q ="""
            INSERT INTO books(title, author, genre, published_year)
            VALUE (%s,%s,%s,%s)
            """
            values = (book.title, book.author,book.genre,book.published_year)
            cursor.execute(q,values)
            self.conn.commit()

        except Exception as e:
            print(e)


    def save_books(self, book_list:list[Book]):
        ''' speichert alle Datensätze der übergebenen book_list'''
        #executemany
        try:
            cursor = self.conn.cursor()
            q = """
            INSERT INTO books (title, author, genre, published_year)
            VALUES (%s,%s,%s,%s)
            """
            values = [(b.title, b.author, b.genre,b.published_year) for b in book_list]
            cursor.executemany(q,values)
            self.conn.commit()
            cursor.close()

        except Exception as e:
            
            print(e)






    def find_all(self)->list[Book]:
        try:
            cursor = self.conn.cursor()# self.conn.cursor(dictionary=True)



        except Exception as e:
            print(e)
        finally:
            if cursor is not None:
                cursor.close()
