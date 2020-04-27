from pymessenger.bot import Bot
import os

ACCESS_TOKEN = os.getenv(ACCESS_TOKEN)
VERIFY_TOKEN = os.getenv(VERIFICATION_TOKEN)
ADMIN = os.getenv(ADMIN)

#SQL Database
import mysql.connector
connection = mysql.connector.connect(user= os.getenv(DB_USER),
                                     password= os.getenv(DB_PASS),
                                     host= os.getenv(DB_HOST),
                                     db= os.getenv(DB))

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



