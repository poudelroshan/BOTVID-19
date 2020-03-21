import sqlite3 as sql

connection = sql.connect("USERS.db")
cursor = connection.cursor()

def add_user(user_id, user_role="user"):
    with connection:
        cursor.execute("INSERT INTO users VALUES(?, ?)", (user_id, user_role))
    return "User Added to Database"

def remove_user(user__id):
    with connection:
        cursor.execute("DELETE FROM users WHERE user_id = ?", (user__id,))
    return "User Removed from Database"

def is_user_subscribed(user__id):
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user__id,))
    if len(cursor.fetchall()) == 1:
        return True
    return False

def get_user_role(user__id):
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user__id,))
    return cursor.fetchall()[0][1]

def get_total_users():
    cursor.execute("SELECT * FROM users")
    return len(cursor.fetchall())

