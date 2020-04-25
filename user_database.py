import authenticate

connection = authenticate.connection
cursor = connection.cursor()

'''
#ONLY USE FOR THE FIRST TIME TO CREATE THE TABLE
cursor.execute("""CREATE TABLE users(user_id int)""")
connection.commit()                                                     
'''

def add_user(user_id):
    with connection:
        cursor.execute("INSERT INTO users VALUES (%s)", (user_id,))
    print("User Added to Database")

def remove_user(user__id):
    with connection:
        cursor.execute("DELETE FROM users WHERE user_id = %s", (user__id,))
    print("User Removed from Database")

    
def is_user_subscribed(user__id):
    with connection:
        cursor.execute("SELECT * FROM users WHERE user_id= %s", (user__id,))
        a = len(cursor.fetchall())
    return a == 1
        
def get_total_users():
    with connection:
        cursor.execute("SELECT * FROM users")
        a = len(cursor.fetchall())
    return a

def get_users():
    with connection:
        cursor.execute("SELECT user_id FROM users")
        return [x[0] for x in cursor.fetchall()] 
    





