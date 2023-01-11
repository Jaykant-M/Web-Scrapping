# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 22:33:25 2022

@author: JaykantMENDAPRA
"""


#####################################
#   Importing required libraries    #
#####################################

from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium import webdriver
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd


######################################################
#   Using driver to open url and open booking.com    #
######################################################

driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://www.booking.com/"

driver = webdriver.Chrome('C:/Users/jmjay/M2S1/Session - Web scrapping/chromedriver_win32/chromedriver')
driver.get(url)
time.sleep(3)


####################################################################################
#   Find the search box to enter city name - change city name as per requirement   #
####################################################################################

element = driver.find_element(By.CSS_SELECTOR,'#ss')
city_name = "paris"
element.send_keys(city_name)

##################################
#   Selecting consent option     #
##################################

ActionChains(driver).click(driver.find_element(By.ID,'onetrust-accept-btn-handler')).perform()


##############################################
#   Selecting check-in and check-out date    #
##############################################

### For the current project we are manually selecting date (11/01/2023)for scrapping the data
####Automate the date selection process
ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR,'#frm > div.xp__fieldset.js--sb-fieldset.accommodation > div.xp__dates.xp__group > div.xp__dates-inner > div:nth-child(2) > div > div > div > div > span')).perform()
ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR,'#frm > div.xp__fieldset.js--sb-fieldset.accommodation > div.xp__dates.xp__group > div.xp-calendar > div > div > div.bui-calendar__content > div:nth-child(1) > table > tbody > tr:nth-child(3) > td.bui-calendar__date.bui-calendar__date--today')).perform()

#   Clicking on search button    #
ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR,'#frm > div.xp__fieldset.js--sb-fieldset.accommodation > div.xp__button > div.sb-searchbox-submit-col.-submit-button > button > span.js-sb-submit-text')).perform()
time.sleep(2)


###########################################################################
#    Creating lists to add information regarding available properties     #
###########################################################################

property_name = []
preferred_plus_property = []
property_stars = []
property_address = []
dist_from_center = []
metro_access = []
booking_reviews = []
user_reviews = []
room_type = []
bed_type = []
sus_property_type = []
property_rating = []
price_per_night = []
breakfast_included = []
free_cancellation_no_prepayment = []


content = driver.page_source        #download and interpret the html code
soup = BeautifulSoup(content) 

# Getting total number of pages for the available properties
total_pages = int(soup.findAll('button',attrs={"class":"fc63351294 f9c5690c58"})[-1].get_text())

##########################################################
#    Iterating through each page to extract the data     #
##########################################################

for x in range(total_pages):
    content = driver.page_source        #download and interpret the html code
    soup = BeautifulSoup(content)       #give the parsed code to beautifulsoup
    
    #Listing all the properties
    props = soup.findAll("div",attrs = {"class":"a826ba81c4 fe821aea6c fa2f36ad22 afd256fc79 d08f526e0d ed11e24d01 ef9845d4b3 da89aeb942"})

    #### Iterating through each property on the page to extract the data
    for x in range(len(props)):
        ##### Extracting Property name
        property_name.append(props[x].findAll("div",attrs = {"class":"fcab3ed991 a23c043802"})[0].get_text())
        
        
        ##### Extracting if the property is preferred parter/plus Property
        ## 0 - Not a preferred partner property
        ## 1 - Preferred partner property
        ## 2 - preferred partner Plus property
        if len(props[x].findAll("span",attrs={"data-testid":"preferred-badge"}))==1:
            preferred_plus_property.append(1)
        else: preferred_plus_property.append(0)
        
        
        ##### Extracting #stars for the property
        if(len(props[x].findAll("span",attrs={"class":"b6dc9a9e69 adc357e4f1 fe621d6382"})))!=0:
            property_stars.append(len(props[x].findAll("span",attrs={"class":"b6dc9a9e69 adc357e4f1 fe621d6382"})))
        else: property_stars.append("No Rating available")
        
        
        ##### Extracting address of the property
        property_address.append(props[x].findAll("span",attrs={"class":"f4bd0794db b4273d69aa"})[0].get_text())
        
        
        ##### Extracting the distance from cente
        #if len(props[x].findAll("span",attrs={"class":"f4bd0794db"})[-2].get_text().split(" ")[0]) == 4:    
        dist_from_center.append(float(props[x].findAll("span",attrs={"data-testid":"distance"})[0].get_text().split(" ")[0]))
        
        
        ##### Checkig for metro access
        if props[x].findAll("span",attrs={"class":"cb5ebe3ffb"})[-1].get_text() == 'Metro access':
            metro_access.append(1)
        else: metro_access.append(0)
        
        
        ##### Checkig for reviews
        if len(props[x].findAll("div",attrs={"class":"b5cd09854e f0d4d6a2f5 e46e88563a"})) != 0:
            booking_reviews.append(props[x].findAll("div",attrs={"class":"b5cd09854e f0d4d6a2f5 e46e88563a"})[0].get_text())
            user_reviews.append(props[x].findAll("div",attrs={"class":"d8eab2cf7f c90c0a70d3 db63693c62"})[0].get_text().split(" ")[0])
        else: 
            booking_reviews.append(0)
            user_reviews.append(0)
        
            
        
        ##### Checkig for room and bed type
        room_type.append(props[x].findAll("span",attrs={"class":"df597226dd"})[0].get_text())
        bed_type.append(props[x].findAll("div",attrs={"class":"cb5b4b68a4"})[0].get_text())
        
        
        ##### Checkig if the property is a travel sustainable property
        if len(props[x].findAll("span",attrs={"class":"a51f4b5adb"}))==1:
            if props[x].findAll("span",attrs={"class":"a51f4b5adb"})[0].get_text() == "Travel Sustainable property":
                sus_property_type.append(1)
            else: pass
        else:
            sus_property_type.append(0)
    
    
        ##### Checkig for property rating
        if len(props[x].findAll("div",attrs={"class":"b5cd09854e d10a6220b4"})) != 0:
            property_rating.append(float(props[x].findAll("div",attrs={"class":"b5cd09854e d10a6220b4"})[0].get_text()))
        else:
            property_rating.append(0)
        
        ##### Checkig for metro access
        if props[x].findAll("div",attrs = {"class":"e6e585da68"})[-1].get_text().find("Original") == -1:
            price_per_night.append(int(props[x].findAll("div",attrs = {"class":"e6e585da68"})[-1].get_text().split(" ")[-1][2:].replace(",","")))
        else:price_per_night.append(int(props[x].findAll("div",attrs = {"class":"e6e585da68"})[-1].get_text().split(" ")[-1][2:-1].replace(",","")))

        ##### Checkig if breakfast is included
        if(len(props[x].findAll("span",attrs={"class":"e05969d63d"})) == 1):
            breakfast_included.append(True)
        else: breakfast_included.append(False)
        
        ##### Checkig if there is free cancellation iption or no prepayment
        if(len(props[x].findAll("div",attrs={"class":"d506630cf3"})) == 1):
            free_cancellation_no_prepayment.append(True)
        else: free_cancellation_no_prepayment.append(False)
        
    
    
    
    # Navigating to next page and waiting for 2 seconds for page to load
    ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR,'#search_results_table > div:nth-child(2) > div > div > div > div.d7a0553560 > div.a826ba81c4.fa71cba65b.fa2f36ad22.afd256fc79.d08f526e0d.ed11e24d01.ef9845d4b3.b727170def > nav > div > div.f32a99c8d1.f78c3700d2 > button')).perform()
    time.sleep(2)

######################################################################
#   Creating a dictionary to store all the information extracted     #
#   creating a dataframe and extracting everything into excel file   #
######################################################################

prop_dict  = {
    "property_name" :           property_name,
    "preferred_plus_property" : preferred_plus_property,
    "property_stars" :           property_stars,
    "property_address" :        property_address,
    "dist_from_center" :        dist_from_center,
    "metro_access" :            metro_access,
    "booking_reviews" :         booking_reviews,
    "user_reviews" :            user_reviews,
    "room_type" :               room_type,
    "bed_type" :                bed_type,
    "sus_property_type" :       sus_property_type,
    "property_rating" :         property_rating,
    "price_per_night" :         price_per_night,
    "breakfast_included" :      breakfast_included,
    "free_cancellation_no_prepayment": free_cancellation_no_prepayment
              }

df = pd.DataFrame(prop_dict)
df.to_excel(f"{city_name}_properties.xlsx",index = False)
df.to_csv(f"{city_name}_properties.csv",index = False)