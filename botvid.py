from flask import Flask, request, render_template
from pymessenger.bot import Bot
import authenticate, user_database, state_database


app = Flask(__name__)
bot = authenticate.verify_bot_access()


# Sends the response to recipient_id using Pymessenger API
def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "Message Sent!"


# Fetches the data from database for the user
def get_message():
    response = state_database.get_tabulated_data()
    return response

# Fetches appropriate data for the admin
def get_sudo_message(message):
    if message == "sudo gtu":
        # 1) "sudo gtu" -> get total numbers of users from database
        response = user_database.get_total_users()
    elif message == "sudo gu":
        # 2) "sudo gu" -> return list of user_ids from database
        response = user_database.get_users()
    elif message == "sudo status":
        # 3) "sudo status" -> Is the bot working?
        response = "Hey, Roshan! BOTVID-19 is working great! :)"
    else:
        response = "unrecognized admin command"
    return response


# Webhook for GET & POST requests
# Verifies the GET/POST requests came from messenger ID of the Bot
# Handles the message receiving and message sending through helper functions
@app.route("/webhook", methods = ["GET", "POST"])
def receive_message():
    # The webhook is set to https://mywebsite.com/webhook
    # If there's a GET request from facebook, it will be of the form:
    # https://mywebsite.com/?hub.mode=subscribe&hub.challenge=906893502&hub.verify_token=VERIFY_TOKEN
    if request.method == "GET":
        return authenticate.verify_fb_token(request) # Authenticate holds verification data
    # If the request was not GET, it was POST
    # In this case, just receive the message from user and respond accordingly
    else:
        output = request.get_json()
        message = "DEFAULT MESSAGE" # Place holder for messages from users
        try: # Grab the text messages only
            message = output["entry"][0]["messaging"][0]["message"]["text"].lower()
        except: # If there is emoji or pictures, ignore it
            pass
        user_id = int(output["entry"][0]["messaging"][0]["sender"]["id"]) #Extracting user ID
        print("The user id is: ", user_id)
        if message == "DEFAULT MESSAGE": # User sent a picture or an emoji
            send_message(user_id, "Sorry! I cannot currently handle non-text messages")
        elif message == "hi" or "hello":
            send_message(user_id, message + " there!")
        elif message == "subscribe": 
            subscribe(user_id)
        elif message == "unsubscribe":
            unsubscribe(user_id)
        elif message == "update":
            response = get_message()
            send_message(user_id, response)
            send_message(user_id, "Above data was scraped from https://www.worldometers.info/coronavirus/country/us/")
        elif message.split()[0] == "sudo" and authenticate.is_admin(user_id):
            # Allow for admins to check bot status using messenger
            response = get_sudo_message(message)
            send_message(user_id, response)
        else: # Unsupported text message
            send_message(user_id, "Sorry! I am a dumb bot, and I didn't quite understand what you just said.")
            send_message(user_id, "Send 'subscribe' to subscribe for periodic notifications, 'update' to get updates about COVID-19, and 'unsubscribe' to unsubscribe from periodic notifications")
            
        return "Message Processed"

# Check whether the user_id is stored in database    
def is_user_subscribed(user_id):
    return user_database.is_user_subscribed(user_id)

# Add user_id to the database
def subscribe(user_id):
    if not (is_user_subscribed(user_id)):
        user_database.add_user(user_id)
        send_message(user_id, "Success! I will now send you periodic messages :)")
        # Realtime console output:
        print("User added to the database!") 
        print("Total users in database: " , user_database.get_total_users())
    else:
        send_message(user_id, "You are already a subscriber!")
        print("User already in the database!")
        print("Total users in database: " , user_database.get_total_users())

        
# Remove user_id from the database
def unsubscribe(user_id):
    if (not is_user_subscribed(user_id)):
        send_message(user_id, "Sorry! You are not a subscriber")
        send_message(user_id, "send me 'subscribe' to subscribe for notifications from me")
    else:
        user_database.remove_user(user_id)
        send_message(user_id, "Sorry to see you go :(")
        print("User removed from the database!")
        print("Total users in database: " , user_database.get_total_users())
        
        
        
# This is for privacy-policy        
@app.route("/privacy-policy")
def privacy():
    return render_template("privacy_policy.html")

# This is the main page for the bot
@app.route("/")
def index():
    return render_template("index.html")

if __name__=="__main__":
    app.run(threaded=True) # enable threading for multiple user handling





