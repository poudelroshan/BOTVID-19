import sqlite3 as sql
from tabulate import tabulate

state_abbr ={'Alabama':'AL', 'Alaska':'AK', 'Arizona':'AZ', 'Arkansas':'AR', 'California':'CA', 'Colorado':'CO', 'Connecticut':'CT',
       'Delaware':'DE', 'Florida':'FL', 'Georgia':'GA', 'Hawaii':'HI', 'Idaho':'ID', 'Illinois':'IL', 'Indiana':'IN', 'Iowa':'IA',
       'Kansas':'KS', 'Kentucky':'KY', 'Louisiana':'LA', 'Maine':'ME', 'Maryland':'MD', 'Massachusetts':'MA', 'Michigan':'MI',
       'Minnesota':'MN', 'Mississippi':'MS', 'Missouri':'MO', 'Montana':'MT', 'Nebraska':'NE', 'Nevada':'NV', 'New Hampshire':'NH',
       'New Jersey':'NJ', 'New Mexico':'NM', 'New York':'NY', 'North Carolina':'NC', 'North Dakota':'ND', 'Ohio':'OH',
       'Oklahoma':'OK', 'Oregon':'OR', 'Pennsylvania':'PA', 'Rhode Island':'RI', 'South Carolina':'SC', 'South Dakota':'SD',
       'Tennessee':'TN', 'Texas':'TX', 'Utah':'UT', 'Vermont':'VT', 'Virginia':'VA', 'Washington':'WA', 'West Virginia':'WV',
             'Wisconsin':'WI', 'Wyoming':'WY', 'District Of Columbia': 'DC'}


connection = sql.connect("TABLE.db")
cursor = connection.cursor()

'''
#ONLY USE FOR THE FIRST TIME TO CREATE THE DATABASE
cursor.execute("""CREATE TABLE data_table(STATE text, ABBR text,PREV_CASES int, CURR_CASES int, PREV_DEATHS int, CURR_DEATHS int)""")
connection.commit()
'''

def get_states():
    cursor.execute("SELECT state from data_table")
    untidy_list =  cursor.fetchall()
    tidy_list = []
    for items in untidy_list:
        tidy_list.append(items[0])
    return tidy_list

def add_state_data(state_data):
    state = state_data[0]
    abbr = state_abbr[state]
    prev_cases = 0
    curr_cases = state_data[1]
    prev_deaths = 0
    curr_deaths = state_data[2]
    with connection:
        cursor.execute("INSERT INTO data_table VALUES(?,?,?,?,?, ?)",
                       (state, abbr, prev_cases, curr_cases, prev_deaths, curr_deaths))
    print(state," Added to the Database")

def update_state_data(state_data):
    state = state_data[0]
    prev_cases = get_curr_cases(state)
    curr_cases = state_data[1]
    prev_deaths = get_curr_deaths(state)
    curr_deaths = state_data[2]
    with connection:
        cursor.execute("UPDATE data_table SET PREV_CASES = {} CURR_CASES = {} PREV_DEATHS = {} CURR_DEATHS = {}".format(prev_cases, curr_cases, prev_deaths, curr_deaths))
    
def print_database():
    cursor.execute("SELECT * from data_table")
    data_list = cursor.fetchall()
    for items in data_list:
        print(items)

def get_data():
    cursor.execute("SELECT * from data_table")
    data_list = cursor.fetchall()
    list_for_table = [["State", "Cases", "Deaths"]]
    for items in data_list:
        list_for_table.append([items[1],items[3],items[5]])
    to_send =  tabulate(list_for_table , headers="firstrow")
    return to_send

    
