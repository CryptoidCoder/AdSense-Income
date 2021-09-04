from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import requests
from datetime import date
from itertools import combinations
from itertools import permutations
from itertools import product  
from datetime import datetime
from datetime import date
import parsedatetime
import datefinder
import time
import pandas as pd
import itertools
import re
import numpy as np
import os
import sys

##### Scraps old data
if os.path.exists("IPs.txt"):
        os.remove("IPs.txt")
#####

# Sets up Selenium
opts = FirefoxOptions()
#opts.add_argument("--headless")
driver = webdriver.Firefox(options=opts, executable_path='/home/sawyer/Documents/GitHub_Folder/Python/geckodriver/geckodriver')
URL = ('https://geonode.com/free-proxy-list')



driver.get(URL)
time.sleep(2)

driver.find_element_by_xpath('/html/body/div/div/div/main/div/div[2]/div[2]/div/div[2]/div[1]/label/select').click() # pt1 selects 200 per page
driver.find_element_by_xpath('//*[@id="proxy-per-page"]/option[4]').click()     # pt2 selects 200 per page
time.sleep(2)

driver.find_element_by_xpath('//*[@id="__next"]/div/div/main/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[3]/div/label[3]').click # selects socks4 for simplicity


for y in range (2,12):
    for x in range (1,201):
    # //*[@id="__next"]/div/div/main/div/div[2]/div[2]/div/div[1]/div[4]/table/tbody/tr[1]/td[1]
    # //*[@id="__next"]/div/div/main/div/div[2]/div[2]/div/div[1]/div[4]/table/tbody/tr[1]/td[2]
    # //*[@id="__next"]/div/div/main/div/div[2]/div[2]/div/div[1]/div[4]/table/tbody/tr[2]/td[1]
    # //*[@id="__next"]/div/div/main/div/div[2]/div[2]/div/div[1]/div[4]/table/tbody/tr[2]/td[2]

    # //*[@id="__next"]/div/div/main/div/div[2]/div[2]/div/div[1]/div[4]/table/tbody/tr[200]/td[1]


        ProxyPort_String=('//*[@id="__next"]/div/div/main/div/div[2]/div[2]/div/div[1]/div[4]/table/tbody/tr[')   +  str(x)     + str(']/td[2]')
        ProxyIP_String= str('//*[@id="__next"]/div/div/main/div/div[2]/div[2]/div/div[1]/div[4]/table/tbody/tr[') + str(x)      + str(']/td[1]')

        ProxyPort = driver.find_element_by_xpath(ProxyPort_String).text
        ProxyIP = driver.find_element_by_xpath(ProxyIP_String).text



        OutString = str(ProxyIP) + str(', ') + str(ProxyPort) # formats text for printing to file
        


        print(OutString, file=open('IPs.txt','a'))

    driver.find_element_by_xpath('//*[@id="proxy-per-page"]').click
    # /html/body/div[1]/div/div/main/div/div[2]/div[2]/div/div[2]/div[2]/label/select/option[1]
    # /html/body/div[1]/div/div/main/div/div[2]/div[2]/div/div[2]/div[2]/label/select/option[2]
    
    Page_Number_string = str('/html/body/div[1]/div/div/main/div/div[2]/div[2]/div/div[2]/div[2]/label/select/option[') + str(y) + str(']') # varible to change the page number
    driver.find_element_by_xpath(Page_Number_string).click
    time.sleep(2)
    

#file.close() # closes IPs.txt
driver.close() # closes current selenium window
driver.quit()  # closes current browser session











































