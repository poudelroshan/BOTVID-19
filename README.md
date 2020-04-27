# BOTVID-19

#### Note:
Initially, there were two repositories for this messenger bot: BOTVID-19 (private repo) & BOTVID-20 (public repo). Based on the feedback received, from [u/warpedspoon](https://www.reddit.com/u/warpedspoon), both of these repositories have been merged to a single repository: BOTVID-19 (public repo). This repository is linked to the live version of the bot, and thus, any changes to the files here will be reflected in the bot.

## System Architecture and working
![https://www.youtube.com/watch?v=4HZa8AJ9www](http://i3.ytimg.com/vi/4HZa8AJ9www/maxresdefault.jpg)

The bot has several components:
1. Heroku with automatic deployment from Github enabled
2. MYSQL server using ClearDB MY SQL addon for Heroku
3. Facebook Messenger page [Botvid-19 on Messenger](https://m.me/botvid19)
4. Website to scrape for data [WorldOMeters](https://www.worldometers.info/coronavirus/country/us/)

Each of these components interact with each other for the bot to function properly.

## What this bot solves? / Motivation
I found myself checking [this website](https://www.worldometers.info/coronavirus/country/us/) frequently to get updates about what was the current situation in each state. Visiting this website took some time as I had to open my browser, type in the URL, and go to specific country. I wondered if there was a way to automate things so that I could save myself from visiting the website above. This gave birth to the idea of a messenger bot.

## How users interact with the bot
* The user visits the messenger page for this bot. [Click here](https://m.me/botvid19)
* The user sends 'update' to the bot via messenger
* The bot fetches scraped data from its MYSQL database and responds back to the user
* The bot also handles basic user inputs like 'hi' or 'hello'
* The bot cannot handle non-text messages like emojis or pictures and thus, responds accordingly
* The bot also has message subscription feature built in. Users can send 'subscribe' and 'unsubscribe' to subscribe/unsubscribe for periodic updates from the bot. This feature, though implemented,  is currently broken due to the limitations imposed by facebook on who the bot can send message to.
* The bot prevents subsribed users from subscribing again or unsubscribed users from unsubscribing. 

#### Note to users who try to interact with the bot:
Since the bot has not been approved for message sending by Facebook, currently, only the Admins/Testers of this bot will be able to interact with the bot. For general users, the bot will respond using a Facebook sent automated message about this note. The bot will hopefully be approved by Facebook for message sending by Tuesday, April 27th, 2020.

#### Admin commands for the bot
To make it easier for the admins to check how many users are using the subsciption feature, some commands are built to work within messenger. This saves the admins from having to check the MYSQL database.
* 'sudo status' responds back with some greeting if the bot is working. To check whether the bot is working or not, users may send anything to the bot. However, 'sudo status'  is a more formal way for admins to check whether the bot is working or not.
* 'sudo gtu' responds back with total number of users who have subscribed to the bot. 'subscribe' will increment and 'unsubscribe' will decrement the total user number which is the return value of 'sudo gtu'
* 'sudo gu' responds back with user ids of users subscribed to the bot. This will help in troubleshooting some database errors
* 'sudo _' sudo followed by any random text will generate 'unrecognized admin command' response.

## How everything works under the hood
* The code for the bot resides in this Github repo
* The App is deployed in Heroku, and any changes to the code will trigger a new build of the app in Heroku, which will be automatically deployed
* botvid.py contains the flask app. It is the core of this app. It handles:
  1. webhooks for checking if the message was sent from specified messenger page
  2. HTML handling for index, and privacy-policy page
  3. subscription, messages sending and receiving
* authenticate.py contains sensitive info. about database credentials, Facebook tokens, and Admin user ids. authenticate.py is used everytime there is need for some authentication
* scrapy.py scrapes for data from the specified website, calls other .py files to update data in database
* state_database.py contains methods to interact with state table in the database. The methods include adding new state, updating state cases, updating state deaths, fetching state cases, etc.
* user_database.py contains methods to interact with user table in the database. The methods include adding new user, removing a user, counting total users, getting a list of users, etc.
* MYSQL database contains two tables:
  1. user table: Stores user ids only
  2. state table: stores state name, state abbreviation, previous cases, current cases, previous deaths, and current deaths
* script.py is set to be run every 10 minutes using Heroku scheduler. This will call scrape.py to update the database contents, and users subscribed to the bot will also be sent an update message. (* The latter part of this feature is currently broken due to Facebook restrictions)
* console.py: lets admins interact with the database using terminal. console.py uses args to call different methods from different .py files:
  1. python3 console.py 'help' -> prints available commands	     
  2. python3 console.py 'get_users()' -> prints a list of users from the database
  3. python3 console.py 'get_total_users()' -> prints the total number of subscribers in the database
  4. python3 console.py 'get_update_data()' -> prints what users get when they send 'update'
  5. python3 console.py 'get_all_state_data()' -> prints everything stored in the state table in MYSQL database
		   




