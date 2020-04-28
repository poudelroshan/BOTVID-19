import authenticate
from tabulate import tabulate

connection = authenticate.connection
connection.ping(reconnect=True)
cursor = connection.cursor()

state_abbr = {"Alabama":"AL", "Alaska":"AK", "Arizona":"AZ", "Arkansas":"AR", "California":"CA",
              "Colorado":"CO", "Connecticut":"CT", "Delaware":"DE", "Florida":"FL", "Georgia":"GA",
              "Hawaii":"HI", "Idaho":"ID", "Illinois":"IL", "Indiana":"IN", "Iowa":"IA",
              "Kansas":"KS", "Kentucky":"KY", "Louisiana":"LA", "Maine":"ME", "Maryland":"MD",
              "Massachusetts":"MA", "Michigan":"MI", "Minnesota":"MN", "Mississippi":"MS",
              "Missouri":"MO", "Montana":"MT", "Nebraska":"NE", "Nevada":"NV", "New Hampshire":"NH",
              "New Jersey":"NJ", "New Mexico":"NM", "New York":"NY", "North Carolina":"NC",
              "North Dakota":"ND", "Ohio":"OH", "Oklahoma":"OK", "Oregon":"OR", "Pennsylvania":"PA",
              "Rhode Island":"RI", "South Carolina":"SC", "South Dakota":"SD", "Tennessee":"TN",
              "Texas":"TX", "Utah":"UT", "Vermont":"VT", "Virginia":"VA", "Washington":"WA",
              "West Virginia":"WV", "Wisconsin":"WI", "Wyoming":"WY", "District Of Columbia": "DC",
              "USA Total": "Total"}


'''
#ONLY USE FOR THE FIRST TIME TO CREATE THE DATABASE
cursor.execute("""CREATE TABLE data_table(STATE text, ABBR text,PREV_CASES int, CURR_CASES int, PREV_DEATHS int, CURR_DEATHS int)""")
connection.commit()
'''

def get_state_current_numbers(state):
    data_list = get_clean_data()
    for items in data_list:
        if items[0] == state:
            cases = items[3]
            deaths = items[5]
    return [cases, deaths]
            

def get_state_deaths(state):
    return get_state_current_numbers(state)[1]


def get_state_cases(state):
    return get_state_current_numbers(state)[0]
    
    
def get_states():
    cursor.execute("SELECT state from data_table")
    untidy_list =  cursor.fetchall()
    tidy_list = []
    for items in untidy_list:
        tidy_list.append(items[0])
    return tidy_list


def add_state_data(state_data):
    state = state_data[0]
    try:
        abbr = state_abbr[state]
    except:
        abbr = "??" # Abbr. not in dict.
    prev_cases = 0
    curr_cases = state_data[1]
    prev_deaths = 0
    curr_deaths = state_data[2]
    cursor.execute("INSERT INTO data_table VALUES(%s, %s, %s, %s, %s, %s)",(state, abbr, prev_cases, curr_cases, prev_deaths, curr_deaths))
    print(state," Added to the Database")

    
def update_state_data(state_data):
    state = state_data[0]
    prev_cases = get_curr_cases(state)
    curr_cases = state_data[1]
    prev_deaths = get_curr_deaths(state)
    curr_deaths = state_data[2]
    cursor.execute("UPDATE data_table SET PREV_CASES = %s, CURR_CASES = %s, PREV_DEATHS = %s, CURR_DEATHS = %s WHERE STATE = %s",(prev_cases, curr_cases, prev_deaths, curr_deaths, state))
    connection.commit()



def get_curr_cases(state):
    cursor.execute("SELECT * from data_table WHERE state = %s",(state,))
    curr_cases = cursor.fetchone()[3]
    return curr_cases

def get_curr_deaths(state):
    cursor.execute("SELECT * from data_table WHERE state = %s", (state,))
    curr_deaths = cursor.fetchone()[5]
    return curr_deaths

        
# Returns database without tabulate applied
def get_clean_data(): 
    cursor.execute("SELECT * from data_table")
    data_list = cursor.fetchall()
    return data_list
        

# Returns database with tabulate applied
def get_tabulated_data():
    connection = authenticate.connection
    connection.ping(reconnect=True)
    cursor = connection.cursor()
    cursor.execute("SELECT * from data_table")
    data_list = cursor.fetchall()
    list_for_table = [["State", "Cases", "Deaths"]]
    for items in data_list:
        list_for_table.append([items[1],items[3],items[5]])
    to_send =  tabulate(list_for_table , headers="firstrow")
    return to_send

    
def get_all_state_data():
    connection = authenticate.connection
    connection.ping(reconnect=True)
    cursor = connection.cursor()
    cursor.execute("SELECT * from data_table")
    data_list = cursor.fetchall()
    list_for_table = [["State", "Abbr.", "Prev. Cases", "Curr. Cases",  "Prev.Deaths", "Curr. Deaths"]]
    for items in data_list:
        list_for_table.append([items[0], items[1], items[2], items[3], items[4], items[5]])
    to_send = tabulate(list_for_table, headers="firstrow") #removed tabulate here
    return to_send

