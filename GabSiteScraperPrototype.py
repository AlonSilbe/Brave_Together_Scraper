#Hello
#Gab.com is a social media and video streaming platform that prides itself on perserving free speech
#Its Non-censorship policy has made it a main site for holocaust denirs
#This site scrapes results from a search in one of the search engines of the site gab trends

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
import time
import pandas as pd


def gabDriverSearch(search_term):
#The Url for serching. The search term entered by user will be added to the url to find its results
    url="https://trends.gab.com/search/item?q={}".format(search_term)
#open chrome with web driver. Driver can be downloaded at: https://chromedriver.chromium.org/downloads
    driver=webdriver.Chrome(executable_path=r"C:\Users\Alon1000\Desktop\chromedriver.exe")
#open site

    driver.get(url)
    #the list where the results will go to
    lis=list()
    #find the html element wich says how many results are on the page
    num=driver.find_elements_by_xpath('/html/body/div[1]/div/div[3]/div')
    #fetch the text you want from the element (number in first tto charachters)
    for nu in num:
        limit=int(nu.text[:2])
    i=0
    #scrape each resukt of the search
    while i<limit:
        #find the html element with the results
         ka=driver.find_elements_by_xpath('/html/body/div[1]/div/ul/li[{}]/div[2]/div[1]/a'.format(i))
         #fetch the text you want from the element and add to the list
         for t in ka:
             lis.append(t.text)
         i=i+1
    #close web -browser
    driver.quit()
    #print the list to see if it came out good 
    print(lis)
    #add list to a directory in ordere to make it fit too be added into a csv file
    dict={"Content":lis}
    #create data-frame based on the list
    df = pd.DataFrame(dict)
    #add dataframe with the results into a csv file
    df.to_csv('results.csv')
 
#holohoax is  a known hashtag for holocaust denial
search_term="holohoax"
#initiate scraper
gabDriverSearch(search_term)
