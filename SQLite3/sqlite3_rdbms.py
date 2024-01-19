'''
* SQLite3 is a Relational Database Management System.(RDBMS)

* We write the SQL queries with uppercase letters because we can easily
distinguish them from the table name and columns.
'''
import sqlite3 as sql
import sqlite3 as lte
import sqlite3 # We will use this one

# Connection
db = sqlite3.connect('./SQLite3/database.db') 
'''
Database name and 
extension can be anything like 'cem.sql', 'ali.sqlite', 'alicem.koyun'.
For convention it is best to use with .db file extension.
This creates db if there is no db with a same name and connects.If exists
then just connects.
'''
db = sqlite3.connect(':memory:')
# This creates db on RAM temporarily. After closing the db this temporary
# db is deleted.

db = sqlite3.connect('')
# This creates db on disk temporarily. After closing the db this temporary
# db is deleted.

db = sqlite3.connect('./SQLite3/database.db') 
# As we know on the 9th line this creates the db if not exits. And it 
# is not deleted.



# Creating Cursor
cr = db.cursor() # We instantiate the cursor object from our database
for i in dir(cr):
    if i.startswith('_'):
        continue
    #or we can use 
        #pass
    else:
        print(i)
'''
Output:
arraysize
close
connection
description
execute
executemany
executescript
fetchall
fetchmany
fetchone
lastrowid
row_factory
rowcount
setinputsizes
setoutputsize
'''


# Creating Table
# Lets do everything from beginning.
import sqlite3

db = sqlite3.connect("./SQLite3/database.db")
cr = db.cursor()
#cr.execute("CREATE TABLE adress_book(name, surname)")
#cr.execute("CREATE TABLE 'employee'('name', 'surname', 'city')")
# This create table commands wont work on second run because table has 
# already been created on the first run. It will raise an error.To prevent
# this error from happening we will create the query like below:
query = ''' CREATE TABLE IF NOT EXISTS
            employee(name, surname, city)'''
cr.execute(query) # Creates the table with given credentials.



# Entering data to the table.
import sqlite3

db = sqlite3.connect('./SQLite3/database.db')
cr = db.cursor()
create_table = '''CREATE TABLE IF NOT EXISTS
                employee(name, surname, city)'''
enter_data = '''INSERT INTO employee VALUES
                ('Alicem', 'Koyun', 'Ankara')'''
                
cr.execute(create_table)
cr.execute(enter_data)
# Even after these steps, if we look at out database with SqliteBrowser
# we will see the empty table. Because we didn't commit() and close()
# the database that we are working on.
db.commit()
db.close()

# In order to not close() everytime we can use context manager of sqlite.
with sqlite3.connect('./SQLite3/database.db') as db:
    cr = db.cursor()
    cr.execute('''CREATE TABLE IF NOT EXISTS
                employee(name, surname, city)''')
    cr.execute('''INSERT INTO employee VALUES
                ('Alicem', 'Koyun', 'Ankara')''')
    db.commit() # We dont need to use db.close() thanks to __exit__ method.



# Queries With Parameters
datas = [('Ali', 'Cem', 'Ankara'), ('Cem', 'Ali', 'Vancouver'), ('Mec', 'Ila', 'USA')]

with sqlite3.connect('./SQLite3/database.db') as db:
    cr = db.cursor()
    for data in datas:
        cr.execute('''INSERT INTO employee VALUES
                    (?, ?, ?)''', data)
    db.commit()



# Selecting and Fetching The Values From Table
# We can get values from table after commit().

# Fetchall Method
with sqlite3.connect('./SQLite3/database.db')as db:
    cr = db.cursor()
    cr.execute('SELECT * FROM employee')
    datas = cr.fetchall()
print(datas)
# [('Alicem', 'Koyun', 'Ankara'), ('Alicem', 'Koyun', 'Ankara'), ('Ali', 'Cem', 'Ankara'), ('Cem', 'Ali', 'Vancouver'), ('Mec', 'Ila', 'USA')]

# Fetchone Method
'''
If we connect a database from outside which we don't know about the 
content, we can use sqlite_master's name column to see how many tables
inside.Hence, we can get the values from the table that we need.But what
if that table contains millions of data if we use fetchall().That'll be
mistake. So we better use fetchone() method to get datas one by one.
By the way sqlite_master, as we can see through the SqliteBrowser, contains
*type = table
*name = employee
*tbl_name = employee
*rootpage = 2
*sql = CREATE TABLE employee(name, surname, city)
but to see the tables from unknown db we ll use the name column only.
'''
with sqlite3.connect('./SQLite3/database.db')as db:
    cr = db.cursor()
    cr.execute('SELECT name FROM sqlite_master')
    print(cr.fetchall()) # [('employee',)]
    cr.execute('SELECT * FROM employee')
    print(cr.fetchone()) #('Alicem', 'Koyun', 'Ankara')
    print(cr.fetchone()) #('Alicem', 'Koyun', 'Ankara')
    print(cr.fetchone()) #('Ali', 'Cem', 'Ankara')
    print(cr.fetchone()) #('Cem', 'Ali', 'Vancouver')

# Fetchmany Method
with sqlite3.connect('./SQLite3/database.db')as db:
    cr = db.cursor()
    cr.execute('SELECT * FROM employee')
    print(cr.fetchmany(5)) # returns the first 5 object from employee table.
    #[('Alicem', 'Koyun', 'Ankara'), ('Alicem', 'Koyun', 'Ankara'), ('Ali', 'Cem', 'Ankara'), ('Cem', 'Ali', 'Vancouver'), ('Mec', 'Ila', 'USA')] 


# Get the value with for loop:
with sqlite3.connect('./SQLite3/database.db')as db:
    cr = db.cursor()
    cr.execute('SELECT * FROM employee')
    for data in cr: # list with tuple datas.
        print(data) # returns tuple data 

# OR 
with sqlite3.connect('./SQLite3/database.db')as db:
    cr = db.cursor()
    cr.execute('SELECT * FROM employee')
    for i in range(5): # returns the first 5 data
        print(cr.fetchone()) # returns data in tuple
        
        
        
# Filtering Data
'''
syntax = SELECT * FROM table_name_from_sqlite_master WHERE column_name = wanted_data
'''

db = sqlite3.connect('./SQLite3/database.db')
cr = db.cursor()
cr.execute('SELECT name FROM sqlite_master') # to find all tables, we know that.
print(cr.execute('SELECT sql FROM sqlite_master').fetchone())
#('CREATE TABLE employee(name, surname, city)',)
cr.execute('''SELECT * FROM employee WHERE city ='Vancouver' ''')
print(cr.fetchall()) # [('Cem', 'Ali', 'Vancouver')] or we could've been
#extract the value using for loop from cr itself.
