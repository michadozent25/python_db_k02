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
            cursor = self.conn.cursor(dictionary=True)# self.conn.cursor(dictionary=True) -> später Entpacken!
            q =  "SELECT * FROM books"
            cursor.execute(q)
            result = cursor.fetchall()
            return [Book(**row) for row in result]


        except Exception as e:
            print(e)
        finally:
            if cursor is not None:
                cursor.close()
    def delete_by_id(self,id:int)-> bool:
        """
        Args:
            id: Primary Key from book
        Return:
            True, wenn erfolgreich gelöscht
        Raise:
        
        """
        try:
            cursor = self.conn.cursor()
            q ="DELETE FROM BOOKS WHERE id =%s"
            cursor.execute(q, (id,) )
            self.conn.commit()
            del_rows = cursor.rowcount
            return del_rows == 1 # True if 1 dataset deleted
        except Exception as e:
            print(e)
        finally:
            if cursor is not None:
                cursor.close()