from tkinter import *
import sqlite3


connect = sqlite3.connect("5/users_tk.db")
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


def add_user(cursor, name, surname, age):
    command = """
        INSERT INTO Users (name, surname, age)
        VALUES (?, ?, ?);
    """
    try:
        cursor.execute(command, (name, surname, age))
    except sqlite3.OperationalError:
        create_table(cursor)
    connect.commit()


win = Tk()
win.geometry("400x400")
win.resizable(0, 0)

entry_name = Entry()
entry_name.pack()

entry_surname = Entry()
entry_surname.pack()

entry_age = Entry()
entry_age.pack()


def add_to_db():
    name = entry_name.get()
    sur = entry_surname.get()
    age = entry_age.get()
    add_user(cursor, name, sur, age)


but = Button(text="Добавить", command=add_to_db)
but.pack()


win.mainloop()