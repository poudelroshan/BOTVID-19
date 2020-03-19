from flask import Flask, request
import random
from pymessenger.bot import Bot
import scrape

bot = Flask(__name__)
ACCESS_TOKEN = 'EAAC2IRS5gxsBALVHI2sJqMXxZAPxOiY3S09OC9nBJfSSdpi5dfRa4QKOF8xKu1nnnHQS6DV0VqqOVLAZAIOF4YXxOFhz9uc1O31sowh3cZBCo0TnONyyOdZA0lQFvjLZCGRPsqe1nXgpZCUxR5eUmuEK6tWvksBAHVAgd5bb5ugwZDZD'
VERIFY_TOKEN = 'thisistherandomlytypedverificationtoken!'
my_bot = Bot(ACCESS_TOKEN)

#Matches VERIFY_TOKEN with Verification token provided to Fb for web Hook
#This ensures that the bot only responds to requests from messenger
def verify_fb_token(token_sent):
    if (token_sent == VERIFY_TOKEN):
    #verification token matches, return expected message
        return request.args.get("hub.challenge")
    #Verification token doesn't match
    return ("Invalid verification token") 


def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "Message Sent!"
    
def get_message():
    prin = scrape.corona()
    return prin

@bot.route('/', methods = ['GET', 'POST'])
def receive_message():
    #If there is a GET request at https://somewebsite.com/
    #And if it's a request from facebook, it will be of the form:
    #https://somewebsite.com/?hub.mode=subscribe&hub.challenge=906893502&hub.verify_token=VERIFY_TOKEN
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    #If the request was not GET, it's POST
    #In this case, just receive the message from user and respond
    else:
        output = request.get_json()
        print(output)
        """
        message = output['entry'][0]['changes'][0]['value']['message']
        user_id = output['entry'][0]['changes'][0]['value']['from']['id']
        
        if message == "Would you rather fight 1 horse-sized duck or 100 duck-sized horses?": #Send Corona Updates:
            response_to_user = get_message()
            send_message(user_id, response_to_user)"""
    return "Message Processed"


if __name__=="__main__":
    bot.run(threaded=True)
    


