# Lets create the context manager on Sqlite to close the connection

import sqlite3
import logging
from contextlib import contextmanager

## To create the table name blog
# connection = sqlite3.connect('application.db')
# cursor = connection.cursor()
# create_table_query = '''
# CREATE TABLE IF NOT EXISTS blog(
#     id INTEGER PRIMARY KEY,
#     blogname TEXT NOT NULL,
#     email TEXT NOT NULL
# );
# '''
# cursor.execute(create_table_query)
# connection.commit()
# connection.close()


# Basic
def main():
    logging.basicConfig(level=logging.INFO)
    connection = sqlite3.connect("application.db")
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM blog')
        logging.info(cursor.fetchall())
    finally:
        logging.info("Closing the connection.")
        connection.close()

# Class 
class SQLite:
    
    def __init__(self, filename:str):
        self.filename = filename
        self.connection = sqlite3.connect(self.filename)

    def __enter__(self): # Setup 
        logging.info("Calling __enter__")
        return self.connection.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb): # Teardown
        logging.info("Calling __exit__")
        self.connection.commit()
        self.connection.close()

def class_method():
    logging.basicConfig(level=logging.INFO)
    with SQLite(filename='application.db') as cursor:
        cursor.execute("SELECT * FROM blog")
        logging.info(cursor.fetchall())


# @contextmanager
@contextmanager
def deco_context(filename:str):
    connection = sqlite3.connect(filename)
    try:
        cursor = connection.cursor()
        yield cursor
    except sqlite3.DatabaseError as error:
        logging.error(error)
    finally:
        logging.info('Closing the connection')
        connection.commit()
        connection.close()
    
def decontext():
    logging.basicConfig(level=logging.INFO)
    with deco_context('application.db') as cursor:
        cursor.execute("SELECT * FROM blog")
        logging.info(cursor.fetchall())




if __name__ == '__main__':
    #main()
    #class_method()
    decontext()