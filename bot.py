from flask import Flask, request, render_template
from pymessenger.bot import Bot
import scrape, authenticate, data, database

app = Flask(__name__)
bot = authenticate.verify_bot_access()


def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "Message Sent!"
    
def get_message(recipient_id, message):
    if authenticate.is_admin(recipient_id) and message.lower() == "sudo":
        response = "Hello, Roshan! The bot is working"
    else:
        response = database.get_data()
        
    return response

@app.route('/webhook', methods = ['GET', 'POST'])
def receive_message():
    #If there is a GET request at https://somewebsite.com/
    #And if it's a request from facebook, it will be of the form:
    #https://somewebsite.com/?hub.mode=subscribe&hub.challenge=906893502&hub.verify_token=VERIFY_TOKEN
    if request.method == 'GET':
        return authenticate.verify_fb_token(request)
    #If the request was not GET, it's POST
    #In this case, just receive the message from user and respond
    else:
        output = request.get_json()
        message = "DEFAULT MESSAGE" #Place holder for messages from users
        try: #grab the text messages only
            message = output['entry'][0]['messaging'][0]['message']['text'].lower()
        except: #If there is emoji or pictures, ignore it
            pass
        user_id = int(output['entry'][0]['messaging'][0]['sender']['id'])

        if message == "DEFAULT MESSAGE":
            send_message(user_id, "Sorry! I cannot currently handle non-text messages :|")
        elif message == "subscribe":
            subscribe(user_id)
        elif message == "unsubscribe":
            unsubscribe(user_id)
        elif message == "update":
            send_message(user_id, "Collecting information from the Internet, please wait.....")
            response = get_message(user_id, message)
            send_message(user_id, response)
        elif message == "sudo":
            response = get_message(user_id, message)
            send_message(user_id, response)
        else: #Unsupported text message
            send_message(user_id, "Sorry! I am a dumb bot, and I didn't quite understand what you just said.")
        return "Message Processed"

def is_user_subscribed(user_id):
    return data.is_user_subscribed(user_id)


def subscribe(user_id):
    if not is_user_subscribed(user_id):
        data.add_user(user_id)
        send_message(user_id, "Success! I will now send you periodic messages :)")
        print("User added to the database!")
        print("Total users in database: " , data.get_total_users())
    else:
        send_message(user_id, "You have already subscribed to our free services!!")
        print("User already in the database!")
        print("Total users in database: " , data.get_total_users())
        
def unsubscribe(user_id):
    if not is_user_subscribed(user_id):
        send_message(user_id, "Sorry! You have not yet subscribed to receive my free updates!!")
        send_message(user_id, "send 'subscribe' to keep updated about the COVID-19 situation")
    else:
        data.remove_user(user_id)
        send_message(user_id, "Sorry to see you go :(")
        print("User removed from the database!")
        print("Total users in database: " , data.get_total_users())

        

@app.route('/privacy-policy')
def privacy():
    return render_template("privacy_policy.html")

@app.route('/')
def index():
    return "<h1> BOTVID-19 is doing his job!!</h1>"

if __name__=="__main__":
    app.run(threaded=True, debug=True)
    


