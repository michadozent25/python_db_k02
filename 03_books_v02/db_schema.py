from mysql.connector import MySQLConnection

def create_new_books_table(conn:MySQLConnection):

    try:
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS books")

        q ="""


            CREATE TABLE `books` (
            `id` int(11) NOT NULL AUTO_INCREMENT,
            `title` varchar(255) DEFAULT NULL,
            `author` varchar(255) DEFAULT NULL,
            `genre` varchar(100) DEFAULT NULL,
            `published_year` int(11) DEFAULT NULL,
            PRIMARY KEY (`id`)
            ) 
        """
        cursor.execute(q)
        cursor.close()
    except Exception as e:
        print(e)