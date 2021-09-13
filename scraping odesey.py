from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
import time
import pandas as pd
import random
def scraper_test(search_term,url1):
#The Url for serching. The search term entered by user will be added to the url to find its results
    url="{}{}".format(url1,search_term)
#open chrome with web driver. Driver can be downloaded at: https://chromedriver.chromium.org/downloads
    driver=webdriver.Chrome(executable_path=r"C:\Users\Alon1000\Desktop\chromedriver.exe")
#open site

    driver.get(url)
    #the list where the results will go to
    lis=list()
    #find the html element wich says how many results are on the page
    limit=50
    i=0
    #scrape each resukt of the search
    while i<limit:
        #find the html element with the results
        
         ka=driver.find_elements_by_xpath('//*[@id="main-content"]/section/section/ul/li[{}]/div/div/div[1]/div[1]/a/div/span'.format(i))
         time.sleep(1)
         #fetch the text you want from the element and add to the list
         time.sleep(1)
         for t in ka:
             h=t.get_attribute('textContent')
             lis.append(h)
             print(h)
             if i>19:
                 driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
             
         i=i+1
    #close web -browser
    driver.quit()
    #print the list to see if it came out good 
    print(lis)
    list_to_csv(lis)

def list_to_csv(lis):
    dict={"Content":lis}
    #create data-frame based on the list
    df = pd.DataFrame(dict)
    time.sleep(1)
    #add dataframe with the results into a csv file
    #tag=str(randint())
    df.to_csv('results_tag_2.csv')
search_term=input('input: ')
url1='https://odysee.com/$/search?q='
scraper_test(search_term,url1)