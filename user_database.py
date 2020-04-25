import authenticate

connection = authenticate.connection
cursor = connection.cursor()

'''
#ONLY USE FOR THE FIRST TIME TO CREATE THE TABLE
cursor.execute("""CREATE TABLE users(user_id int)""")
connection.commit()                                                     
'''

def add_user(user_id):
    connection.ping(reconnect=True)
    with connection:
        cursor.execute("INSERT INTO users VALUES (%s)", (user_id,))
        connection.commit()
    print("User Added to Database")

def remove_user(user__id):
    connection.ping(reconnect=True)
    with connection:
        cursor.execute("DELETE FROM users WHERE user_id = %s", (user__id,))
        connection.commit()
    print("User Removed from Database")

    
def is_user_subscribed(user__id):
    cursor.execute("SELECT * FROM users WHERE user_id= %s", (user__id,))
    return len(cursor.fetchall()) != 0

def get_total_users():
    cursor.execute("SELECT * FROM users")
    return len(cursor.fetchall())
    
    
def get_users():
    connection.ping(reconnect=True)
    with connection:
        cursor.execute("SELECT user_id FROM users")
        return [x[0] for x in cursor.fetchall()]








