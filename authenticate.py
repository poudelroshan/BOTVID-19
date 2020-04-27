from pymessenger.bot import Bot

import os

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
VERIFY_TOKEN = os.environ.get("VERIFICATION_TOKEN")
ADMIN = os.environ.get("ADMIN")

#SQL Database
import mysql.connector
connection = mysql.connector.connect(user= os.environ.get("DB_USER"),
                                     password= os.environ.get("DB_PASS"),
                                     host= os.environ.get("DB_HOST"),
                                     db= os.environ.get("DB"))

def verify_bot_access():
    return Bot(ACCESS_TOKEN)

#Matches VERIFY_TOKEN with Verification token provided to Fb for web Hook                                                                            #This ensures that the bot only responds to requests from messenger
def verify_fb_token(request):
    token_sent = request.args.get("hub.verify_token")
    if (token_sent == VERIFY_TOKEN):
    #verification token matches, return expected message
        return request.args.get("hub.challenge")
    #Verification token doesn't match
    return ("<h1>Access Denied: No Proper Rights!!<h1>")

def is_admin(user_id):
    return user_id == ADMIN



