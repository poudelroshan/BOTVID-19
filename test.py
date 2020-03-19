from flask import Flask, request
import random
from pymessenger.bot import Bot
import scrape

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    return "<h1> This test page works! </h1>"

if __name__ == "__main__":
    app.run(threaded=True)
