import sqlite3

connect = sqlite3.connect("MY.db")
cursor = connect.cursor()


def create_table(cursor):
    command = """
        CREATE TABLE IF NOT EXISTS Users(
            id INTEGER PRIMARY KEY,
            name TEXT,
            surname TEXT,
            age INTAGER
        );
    """
    cursor.execute(command)

def read_all(cursor):
    re = cursor.execute("SELECT * FROM Users;")
    re = re.fetchall()
    for r in re:
        print(r)

def add_user(cursor, name, surname, age):
    command = """
        INSERT INTO Users (name, surname, age)
        VALUES (?, ?, ?);
    """
    cursor.execute(command, (name, surname, age))
    connect.commit()

def delit_all_users(cursor):
    command = "DELITE * FROM Users;"
    cursor.execute(command)

def update_user_name(name, id):
    command = "UPDATE "


# create_table(cursor)
# add_user(cursor, "Я", "Я", 14)
delit_all_users(cursor)
read_all(cursor)    
