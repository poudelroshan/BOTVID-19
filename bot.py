from flask import Flask, request, render_template
from pymessenger.bot import Bot
import scrape, authenticate

app = Flask(__name__)
bot = authenticate.verify_bot_access()


def send_message(recipient_id, response):
    if authenticate.admin(recipient_id):
        response = "Hello, Roshan! The bot is working"
    my_bot.send_text_message(recipient_id, response)
    return "Message Sent!"
    
def get_message():
    prin = scrape.corona()
    return prin

@app.route('/webhook', methods = ['GET', 'POST'])
def receive_message():
    #If there is a GET request at https://somewebsite.com/
    #And if it's a request from facebook, it will be of the form:
    #https://somewebsite.com/?hub.mode=subscribe&hub.challenge=906893502&hub.verify_token=VERIFY_TOKEN
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return authenticate.verify_fb_token(token_sent, request)
    #If the request was not GET, it's POST
    #In this case, just receive the message from user and respond
    else:

        output = request.get_json()
        print(output)

        message = "DEFAULT MESSAGE"
        try:
            message = output['entry'][0]['messaging'][0]['message']['text']
        except:
            pass
        user_id = output['entry'][0]['messaging'][0]['sender']['id']

        print("Message received from user: ")
        print(str(user_id))
        print("Message: " + message)
        
        if message.lower() != "stop":
            response_to_user = get_message()
            send_message(user_id, response_to_user)
    return "Message Processed"

@app.route('/privacy-policy')
def privacy():
    return render_template("privacy_policy.html")

@app.route('/')
def index():
    return "<h1> This page for Corona Bot, Korea works!!</h1>"

if __name__=="__main__":
    app.run(threaded=True, debug=True)
    


