from tabulate import tabulate
import requests, database
from bs4 import BeautifulSoup


URL = "https://www.worldometers.info/coronavirus/country/us/"

def corona():
    page_response = requests.get(URL)
    soup = BeautifulSoup(page_response.content, "html.parser")
    table_body = soup.find('tbody')
    rows = table_body.find_all('tr')
    data_list = []
    for row in rows:
        cols = row.find_all('td')
        cols = [x.text.strip() for x in cols]
        data_list.append([cols[0], cols[1], cols[3]])
    for state_data in data_list:
        update_database(state_data)
        
                
def update_database(state_data):
    state_data = refined(state_data)
    state = state_data[0]
    if (state) not in database.get_states():
        database.add_state_data(state_data)
    else:
        prev_cases = database.get_state_cases(state)
        prev_deaths = database.get_state_deaths(state)
        new_cases = state_data[1]
        new_deaths = state_data[2]
        if (new_cases > prev_cases or new_deaths > prev_deaths):
            database.update_state_data(state_data)
            
    print("Data for " , state, " Updated")

    
def refined(state_data):
    for numbers in state_data[1:]:
        index = state_data.index(numbers) 
        #Remove Commas from numbers
        state_data[index] = numbers.replace(",", "") 
        #Empty strings = number 0
        if numbers == "": 
            state_data[index] = 0
        state_data[index] = int(state_data[index])

        return state_data
        
    
if __name__ == "__main__":
    corona()
