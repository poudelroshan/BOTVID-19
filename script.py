import scrape, bot, user_database

def send_message():
    for users in user_database.get_users():
        bot.send_message(users, bot.get_message())
    print("Sent update message to all users")



if __name__ == '__main__':
    scrape.corona() #update database
    send_message()

    
