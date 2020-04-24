import sqlite3 as sql

connection = sql.connect("TABLE.db")
cursor = connection.cursor()

'''
#ONLY USE FOR THE FIRST TIME TO CREATE THE TABLE
cursor.execute("""CREATE TABLE users(user_id int)""")
connection.commit()                                                     '''


def add_user(user_id):
    with connection:
        cursor.execute("INSERT INTO users VALUES (?)", (user_id,))
    print("User Added to Database")

def remove_user(user__id):
    with connection:
        cursor.execute("DELETE FROM users WHERE user_id = ?", (user__id,))
    print("User Removed from Database")

def is_user_subscribed(user__id):
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user__id,))
    if len(cursor.fetchall()) == 1:
        return True
    return False

def get_total_users():
    cursor.execute("SELECT * FROM users")
    return len(cursor.fetchall())

