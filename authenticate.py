from pymessenger.bot import Bot


ACCESS_TOKEN = 'EAAC2IRS5gxsBAJzFpA0Wz3O8PHN67ZBNw22nSikeOqXHB6kW8OSuJnnx\
CR1ZCDlFexQwoFQ4mFu9Lo2l90KGtUXZAX8kS3kZCQCTu3m0GQZAo0Xm9vIonHRXjFH7EDbUz\
1wHZCuccS1rdnfdXwluZAg84OED1yYPt0G30uc8IvCzgZDZD'
VERIFY_TOKEN = 'thisistherandomlytypedverificationtoken!'

def verify_bot_access():
    return Bot(ACCESS_TOKEN)

#Matches VERIFY_TOKEN with Verification token provided to Fb for web Hook                                                                            #This ensures that the bot only responds to requests from messenger
def verify_fb_token(request):
    token_sent = request.args.get("hub.verify_token")
    if (token_sent == VERIFY_TOKEN):
    #verification token matches, return expected message
        return request.args.get("hub.challenge")
    #Verification token doesn't match
    return ("<h1>Invalid verification token<h1>")

def is_admin(user_id, message):
    if user_id == "2723665511083978" and message.lower() == "sudo":
        return True
    return False


