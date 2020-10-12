import sqlite3

class Person:
    def __init__(self, id_number=-1, first="", last="", age=-1): # Fields with default values
        self.id_number = id_number
        self.first = first
        self.last  = last
        self.age   = age
        self.connection = sqlite3.connect('mydata.db') # If exist an database, it will connect to this database. If does not exist a data base, it will create a new one
        self.cursor = self.connection.cursor() # Cursor is necessary to execute sql query

    def load_person(self, id_number): # Load person from the table and converts into a python object
        self.cursor.execute("""
        SELECT * FROM persons
        WHERE id = {}
        """.format(id_number))

        results = self.cursor.fetchone() # fetch one # buscar um

        self.id_number = id_number # index here is [0]
        self.first = results[1]
        self.last  = results[2]
        self.age   = results[3]

    def insert_person(self):  # insert a new person to the database
        self.cursor.execute("""
        INSERT INTO persons VALUES
        ({}, '{}', '{}', {})
        """.format(self.id_number, self.first, self.last, self.age))

        self.connection.commit()
        self.connection.close()

p1 = Person(7, "Will", "Smith", 45)
p1.insert_person()

connection = sqlite3.connect('mydata.db')
cursor     = connection.cursor()

cursor.execute("SELECT * FROM persons")

results = cursor.fetchall()
print(results)
connection.close()


# p1 = Person()
# p1.load_person(1)
# print(p1.first)
# print(p1.last)
# print(p1.age)
# print(p1.id_number)
# Successful loaded a object from the database into the python script as a python object

####################################################################################

# connection = sqlite3.connect('mydata.db') # If exist an database, it will connect to this database. If does not exist a data base, it will create a new one
# cursor = connection.cursor() # Cursor is necessary to execute sql query

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS persons (
#     id INTEGER PRIMARY KEY,
#     first_name TEXT,
#     last_name TEXT,
#     age INTEGER
# )
# """)

# cursor.execute("""
# INSERT INTO persons VALUES
# (1, 'Ana', 'Paula', 22),
# (2, 'Tenile', 'Egito', 30),
# (3, 'Tereza', 'Raquel', 18),
# (4, 'Joel', 'Silva', 17),
# ('5', 'Hildebrando', 'Silva', 23)
# """)

# cursor.execute("""
# SELECT * FROM persons 
# WHERE last_name = 'Silva'
# """)
# rows = cursor.fetchall() # fetchall means find everything BUSCAR TUDO # fetch all
# print(rows)

# connection.commit() # Apply to the database
# connection.close()