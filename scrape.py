#from time import gmtime, strftime
import datetime, os
from tabulate import tabulate
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



URL = "https://coronamap.site/"


def output(confirmed, recovered, death, time):
    return tabulate([["State", "Cases", "Deaths"], [confirmed.text,death.text,recovered.text],
                     [confirmed.text,death.text,recovered.text],[confirmed.text,death.text,recovered.text]], headers="firstrow")
    
def corona():
    options = Options()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    options.headless = True
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path = os.environ.get("CHROMEDRIVER_PATH"), chrome_options = options)
    
    driver.get(URL)
    english_lang = driver.find_element_by_class_name("english-btn")
    english_lang.click()
    close_button = driver.find_element_by_class_name("notice-btn")
    close_button.click()
    
    confirmed = driver.find_element_by_xpath("/html/body/div[8]/div[1]/div")
    recovered = driver.find_element_by_xpath("/html/body/div[8]/div[2]/div[1]/div[2]")
    death = driver.find_element_by_xpath("/html/body/div[8]/div[2]/div[3]/div[2]")
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M KST")

    value = output(confirmed, recovered, death, time)
    driver.quit()
    return value

if __name__ == "__main__":
    print(corona())

    
