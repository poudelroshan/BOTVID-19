import scrape, botvid, user_database

DISCLAIMER = "The above message was automatically sent because you have subscribed for regular updates from this bot. Send 'unsubscribe' to stop getting future updates"

def send_message():
    for users in user_database.get_users():
        botvid.send_message(users, botvid.get_response())
        botvid.send_message(users, DISCLAIMER)
    print("Sent automated update message to all users")



if __name__ == '__main__':
    scrape.corona() #update database
    send_message()

    
