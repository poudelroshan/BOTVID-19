from flask import flask, request
import random
from pymessenger.bot import Bot
import scrape


test = Flask(__name__)

@test.route('/', methods = ['GET', 'POST'])
def testing():
    return "<h1> Hello this is working!</h1>"

if __name__ == "__main__":
    test.run(threaded = True)
