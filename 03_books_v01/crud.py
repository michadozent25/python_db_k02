from models import Book
class BookRepository:
    def __init__(self,conn):
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



    def find_all(self)->list[Book]:
        try:
            cursor = self.conn.cursor()# self.conn.cursor(dictionary=True)



        except Exception as e:
            print(e)
