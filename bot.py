from flask import Flask, request, render_template
from pymessenger.bot import Bot
import scrape, authenticate, data

app = Flask(__name__)
bot = authenticate.verify_bot_access()


def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "Message Sent!"
    
def get_message(recipient_id, message):
    if authenticate.is_admin(recipient_id) and message.lower() == "sudo":
        response = "Hello, Roshan! The bot is working"
    else:
        response = scrape.corona()
    return response

@app.route('/webhook', methods = ['GET', 'POST'])
def receive_message():
    #If there is a GET request at https://somewebsite.com/
    #And if it's a request from facebook, it will be of the form:
    #https://somewebsite.com/?hub.mode=subscribe&hub.challenge=906893502&hub.verify_token=VERIFY_TOKEN
    if request.method == 'GET':
        send_message("2723665511083978", "I can send a message")
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
            send_message(user_id, "Sorry! I cannot currently handle non-text messages :(")
        elif message == "subscribe":
            subscribe(user_id)
        elif message == "unsubscribe":
            unsubscribe(user_id)
        elif message == "update":
            response = get_message(user_id, message)
            send_message(user_id, message)
        else: #Unsupported text message
            send_message(user_id, "Sorry! I am not smart enough to understand what you said")
    return "Message Processed"

def is_user_subscribed(user_id):
    return data.is_user_subscribed(user_id)


def subscribe(user_id):
    if not is_user_subscribed(user_id):
        data.add_user(user_id)
        send_message(user_id, "Success! You will now receive periodic text messages from me :)")
    else:
        send_message(user_id, "You have already subscribed to our free services!!")
        
def unsubscribe(user_id):
    if not is_user_subscribed(user_id):
        send_message(user_id, "Sorry! You have not yet subscribed to our free services!!")
    else:
        data.remove_user(user_id)
        send_message(user_id, "Success! You have unsubscribed from my periodic messages")
        

@app.route('/privacy-policy')
def privacy():
    return render_template("privacy_policy.html")

@app.route('/')
def index():
    return "<h1> This page for Corona Bot, Korea works!!</h1>"

if __name__=="__main__":
    app.run(threaded=True, debug=True)
    


