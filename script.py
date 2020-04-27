import scrape, botvid, user_database, authenticate
from datetime import datetime

Alert1 = "You received the message above because you have subscribed for periodic notifications from me. The subscription lasts for 24 hours before Facebook unsubscribes you automatically."
Alert2 = "Due to Facebook's Privacy Policy, If you want to keep receiving messages from me, you will need to send me 'subscribe' every 24 hours."

def send_message():
    now = datetime.now()
    mins = now.minute
    hours = now.hour
    # Send updates every 2 even hours (0,2,4,6...) at 12 or 13 minutes ie. 2:12 pm or 2:13 pm and so on
    # Only send updates from 8 AM till 10 PM UTC
    if ((hours % 2 == 0 and (hours > 6 and hours < 24))  and (mins == 12 or mins == 13)):
        for users in user_database.get_users():
            botvid.send_message(users, botvid.get_message())
            botvid.send_message(users, Alert1)
            botvid.send_message(users, Alert2)
            print("Sent automated update message to user: ", users, " at ", now)
            
    print("Database updated at: ", now)
    

if __name__ == '__main__':
    scrape.corona() #update database
    send_message()

    
