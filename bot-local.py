from selenium import webdriver #for browser automation
from selenium.webdriver.chrome.options import Options #for browser automation
from selenium.webdriver.common.keys import Keys #for browser automation
import time #for waiting
#########################

## Definitions:

tabcount = 0

#########################

##Functions:

def updatestatus(statusmessage): #make/ update a file with the current bot status
    file = open('status.txt', "w")
    file.seek(0)
    file.write(statusmessage)
    file.close()


#Browser Functions:
def openbrowser(): #openbrowser but no tabs or sites
    global driver, chrome_options
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(executable_path="D://Coding//Coding//chromedriver.exe", chrome_options=chrome_options)
    
def opengoogle(): #opens google in current tab
    driver.get("https://www.google.com") #go to google.com
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="L2AGLb"]/div').click() #agree to t&c

def opennewtab(site): #open a new tab with a certian site
    global tabcount
    tabcount = tabcount + 1
    print(f"tab = {tabcount}, website = {site}")
    driver.execute_script("window.open('');") # Open a new window
    driver.switch_to.window(driver.window_handles[tabcount]) # Switch to the new window
    driver.get(site)
    
def changeoriginaltab(site): #change first tab
    driver.switch_to.window(driver.window_handles[0])
    print(f"tab = {tabcount}, website = {site}")
    driver.get(site)

def changetab(tab, site): #change a certain tab
    driver.switch_to.window(driver.window_handles[tab])
    print(f"tab {tab} = {site}")
    driver.get(site)

def closebrowsertabs(): #close all tabs and browser window
    global tabcount
    for i in range(tabcount+1):
        tabcount = tabcount - 1
        driver.switch_to.window(driver.window_handles[tabcount])
        driver.close()

def switchtabs(tab): #switch to a certian tab (but don't change it)
    driver.switch_to.window(driver.window_handles[tab])
    print(f"Switched to tab {tab}")




updatestatus("Bot Running")
openbrowser()
changeoriginaltab("https://github.com")
opennewtab("https://adsense-income-cryptoidcoder.netlify.app/")
time.sleep(1)
closebrowsertabs()
updatestatus("Bot Not Running")