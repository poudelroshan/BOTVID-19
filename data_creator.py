import sqlite3

connection = sqlite3.connect("TEST.db")
cursor = connection.cursor()

'''cursor.execute("""CREATE TABLE users(
user_id integer,
user_role text
)""")'''

with connection:
    cursor.execute("INSERT INTO test VALUES (3523, 'user')")
    cursor.execute("INSERT INTO test VALUES (3523, 'user')")
    cursor.execute("INSERT INTO test VALUES (3523, 'user')")
    cursor.execute("INSERT INTO test VALUES (3523, 'user')")
    cursor.execute("INSERT INTO test VALUES (3523, 'user')")
    cursor.execute("INSERT INTO test VALUES (3523, 'user')")



for item in cursor.execute("SELECT * FROM test").fetchall():
    print(item)

