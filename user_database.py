import authenticate

connection = authenticate.connection
cursor = connection.cursor()

'''
#ONLY USE FOR THE FIRST TIME TO CREATE THE TABLE
cursor.execute("""CREATE TABLE users(user_id int)""")
connection.commit()                                                     
'''

def add_user(user_id):
    try:
        cursor.execute("INSERT INTO users VALUES (%s)", (user_id,))
        print("User Added to Database")
    finally:
        connection.close()

def remove_user(user__id):
    try:
        cursor.execute("DELETE FROM users WHERE user_id = %s", (user__id,))
    finally:
        connection.close()
        print("User Removed from Database")

    
def is_user_subscribed(user__id):
    try:
        cursor.execute("SELECT * FROM users WHERE user_id= %s", (user__id,))
        a = len(cursor.fetchall()) == 1
    finally:
        connection.close()
        return a
    
def get_total_users():
    try:
        cursor.execute("SELECT * FROM users")
        a = len(cursor.fetchall())
    finally:
        connection.close()
        return a


def get_users():
    try:
        cursor.execute("SELECT user_id FROM users")
        a = cursor.fetchall()
    finally:
        return [x[0] for x in a] 



