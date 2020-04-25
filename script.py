import scrape, botvid, user_database

def send_message():
    for users in user_database.get_users():
        print(users)
        botvid.send_message(users, "HEY")
    print("Sent update message to all users")



if __name__ == '__main__':
#    scrape.corona() #update database
    send_message()

    
