import authenticate

'''
#ONLY USE FOR THE FIRST TIME TO CREATE THE TABLE
connection = authenticate.connection
connection.ping(reconnect=True)
cursor = connection.cursor()
cursor.execute("""CREATE TABLE users(user_id BigInt)""")
connection.commit()                                                     
'''

def add_user(user_id):
    connection = authenticate.connection
    connection.ping(reconnect=True)
    cursor = connection.cursor()
    print("The following user id is being added")
    cursor.execute("INSERT INTO users VALUES (%s)", (user_id,))
    connection.commit()
    cursor.close()
    connection.close()
    print("User ", user_id, " Added to Database")

def remove_user(user__id):
    connection = authenticate.connection
    connection.ping(reconnect=True)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE user_id = %s", (user__id,))
    connection.commit()
    cursor.close()
    connection.close()
    print("User ", user__id, " Removed from Database")

    
def is_user_subscribed(user__id):
    connection = authenticate.connection
    connection.ping(reconnect=True)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id= %s", (user__id,))
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return len(users) != 0

def get_total_users():
    connection = authenticate.connection
    connection.ping(reconnect=True)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return len(users)
    
    
def get_users():
    connection = authenticate.connection
    connection.ping(reconnect=True)
    cursor = connection.cursor()
    cursor.execute("SELECT user_id FROM users")
    user_ids = cursor.fetchall()
    cursor.close()
    connection.close()
    return [x[0] for x in user_ids]
    




