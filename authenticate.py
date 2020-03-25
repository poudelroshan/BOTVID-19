from pymessenger.bot import Bot

ACCESS_TOKEN = 'EAAC2IRS5gxsBABwSlnbAn0DZC38TEZAWAbrZCYGEBX0nuCA4TtDMMwLGbgy9fKb7zzIlyc4OjTQmu2FoS9R89My0m4AZCrB5VhK6OGR2VxKkvZC9QjBSA5LC7J8qgbkfNiA0DAhqKDBQSPPGhuHZB7WZCWgt7MUJgBPj6gMuKMaZCAZDZD'
VERIFY_TOKEN = 'thisistherandomlytypedverificationtoken!'
ADMIN = 2723665511083978

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
    if user_id == ADMIN:
        return True
    return False


