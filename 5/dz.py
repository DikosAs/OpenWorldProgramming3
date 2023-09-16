import sqlite3

con = sqlite3.connect("data.db")
cursor = con.cursor()

def delete_users_by_name(cursor, user_name):
    cursor.execute("DELETE FROM users WHERE name = '?'", (user_name))


delete_users_by_name(cursor, 'Дмитрий')
con.commit()
