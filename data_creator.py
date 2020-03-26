import sqlite3

connection = sqlite3.connect("numbers.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE corona(
state text,
cases integer,
deaths integer
)""")

with connection:
    cursor.execute("INSERT INTO corona VALUES ('AL', 3200, 222)") #Alabama
    cursor.execute("INSERT INTO corona VALUES ('AK', 3200, 222)") #Alaska
    cursor.execute("INSERT INTO corona VALUES ('AZ', 3200, 222)") #Arizona
    cursor.execute("INSERT INTO corona VALUES ('AR', 3200, 222)") #Arkansas
    cursor.execute("INSERT INTO corona VALUES ('CA', 3200, 222)") #California
    cursor.execute("INSERT INTO corona VALUES ('AL', 3200, 222)") #Alabama
    cursor.execute("INSERT INTO corona VALUES ('AL', 3200, 222)") #Alabama
    cursor.execute("INSERT INTO corona VALUES ('AL', 3200, 222)") #Alabama
    cursor.execute("INSERT INTO corona VALUES ('AL', 3200, 222)") #Alabama
        cursor.execute("INSERT INTO corona VALUES ('AL', 3200, 222)") #Alabama
    cursor.execute("INSERT INTO corona VALUES ('AL', 3200, 222)") #Alabama
    cursor.execute("INSERT INTO corona VALUES ('AL', 3200, 222)") #Alabama
    cursor.execute("INSERT INTO corona VALUES ('AL', 3200, 222)") #Alabama
    cursor.execute("INSERT INTO corona VALUES ('AL', 3200, 222)") #Alabama
    cursor.execute("INSERT INTO corona VALUES ('AL', 3200, 222)") #Alabama
    cursor.execute("INSERT INTO corona VALUES ('AL', 3200, 222)") #Alabama
    cursor.execute("INSERT INTO corona VALUES ('AL', 3200, 222)") #Alabama
    cursor.execute("INSERT INTO corona VALUES ('AL', 3200, 222)") #Alabama
        cursor.execute("INSERT INTO corona VALUES ('AL', 3200, 222)") #Alabama
    cursor.execute("INSERT INTO corona VALUES ('AL', 3200, 222)") #Alabama
    cursor.execute("INSERT INTO corona VALUES ('AL', 3200, 222)") #Alabama
    cursor.execute("INSERT INTO corona VALUES ('AL', 3200, 222)") #Alabama
    cursor.execute("INSERT INTO corona VALUES ('AL', 3200, 222)") #Alabama
    cursor.execute("INSERT INTO corona VALUES ('AL', 3200, 222)") #Alabama
    cursor.execute("INSERT INTO corona VALUES ('AL', 3200, 222)") #Alabama
    cursor.execute("INSERT INTO corona VALUES ('AL', 3200, 222)") #Alabama
    cursor.execute("INSERT INTO corona VALUES ('AL', 3200, 222)") #Alabama
        cursor.execute("INSERT INTO corona VALUES ('AL', 3200, 222)") #Alabama
    cursor.execute("INSERT INTO corona VALUES ('AL', 3200, 222)") #Alabama
    cursor.execute("INSERT INTO corona VALUES ('AL', 3200, 222)") #Alabama
    cursor.execute("INSERT INTO corona VALUES ('AL', 3200, 222)") #Alabama
    cursor.execute("INSERT INTO corona VALUES ('AL', 3200, 222)") #Alabama
    cursor.execute("INSERT INTO corona VALUES ('AL', 3200, 222)") #Alabama
    cursor.execute("INSERT INTO corona VALUES ('AL', 3200, 222)") #Alabama
    cursor.execute("INSERT INTO corona VALUES ('AL', 3200, 222)") #Alabama
    cursor.execute("INSERT INTO corona VALUES ('AL', 3200, 222)") #Alabama








    
    cursor.execute("INSERT INTO test VALUES ('New York', 3200, 222)")
    cursor.execute("INSERT INTO test VALUES ('New York', 3200, 222)")
    cursor.execute("INSERT INTO test VALUES ('New York', 3200, 222)")
    cursor.execute("INSERT INTO test VALUES ('New York', 3200, 222)")
    cursor.execute("INSERT INTO test VALUES ('New York', 3200, 222)")
    cursor.execute("INSERT INTO test VALUES ('New York', 3200, 222)")




for item in cursor.execute("SELECT * FROM test").fetchall():
    print(item)

