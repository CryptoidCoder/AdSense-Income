##Imports:
import time, random #for staying on a site a random amount of time
import requests, json #geting Ip Info
import os, sys #for restarting(Getting a new IP)
from selenium import webdriver #for browser automation
from selenium.webdriver.chrome.options import Options #for browser automation
from selenium.webdriver.common.keys import Keys #for browser automation
from dotenv import load_dotenv #for accessing the .env file for secret api keys & variables

#########################

##Definitions:

tabcount = 0

##.env:
load_dotenv()

dummysitelist = os.getenv('dummysitelist') #list of dummy sites to visit
adsitelist = os.getenv('adsitelist') #all of the sites with ads
bwapikey = os.getenv('bwapikey') #Bitwarden CLI API Key

#print(f"dumymsitelist, adsitelist, bwapikey respectively = \n {dummysitelist} \n {adsitelist} \n {bwapikey} \n \n")


#########################

##Functions:

def addnewline(filename,text): #append text to a new line on a file
    # Open the file in append & read mode ('a+')
    with open(filename, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0 :
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(text)
        file_object.close()


#IP Functions:
def getip(): #get current Public IP address
    response = requests.get('https://ipinfo.io/json', verify = True) #request it from the website (ipinfo.io)

    if response.status_code != 200: #if there isn't a succesful response: return status+error message & exit
        return 'Status:', response.status_code, 'Problem While requesting IP. Exiting.'
        exit()

    data = response.json()

    return data['ip'] #return only the ip from the dataset

def iplistupdate(): #add the current ip into the iplist to say it has been used before
    global iplist
    currentip = getip() #get currnet ip (ip to add to the used list)
    addnewline('iplist.txt', currentip) #add current ip to the list of used Ip addresses
    iplist = getiplist() #update list object iplist using the newly updated .txt file
    print(f"Added {currentip} To the list of used IP Addresses")

def setupbw(): #install & configure bitwarden CLI
    print("Setting up Bitwarden & making sure iplistitem is existent")
    #install bitwarden cli
        #choco install bitwarden-cli
        #sudo snap install bw

    #configure bitwarden
        #bw login --apikey

    #check if the iplist exists
        #try:
            #bw get iplistitem

        #except:
            #bw create iplistitem
            #bw create attachment --file ./iplist.txt --itemid 16b15b89-65b3-4639-ad2a-95052a6d8f66 #--itemid = the item(iplistitem)

def getiplist(): #fetch the iplist
    #setupbw() #make sure bw-cli is all setup

    #get the iplist, from bitwarden (using bitwarden cli)
    #bw get attachment <filename> --itemid <id>
    
    #turn iplist.txt into variable
    global iplist
    file = open('iplist.txt', 'r')
    iplist = []

    while True:
        next_line = file.readline()
        iplist.append(next_line.strip())

        if not next_line:
            break;

    file.close()
    iplist.remove('') #remove blank item
    return iplist

def compareips(): #compare the current ip to the ip list; if it is in the list restart (getting a new ip)
    currentip = getip()
    iplist = getiplist()

    if currentip in iplist: #if ip has been used before, restart(get a new ip)
        try: #try to shutdown PC using linux command
            #os.system("reboot now")
            print("linux shutdown procedure")

        except: 
            try: #use windows shutdown command
                #os.system("shutdown /r /t 0")
                print("windows shutdown procedure")
            
            except: #shutdown using cloud provider API/CLI
                print("Shutting Down via cloud provider API/CLI")


    else:
        iplistupdate()


#Browser Functions:
def openbrowser(): #openbrowser but no tabs or sites
    global driver, chrome_options
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(executable_path="D://Coding//Coding//chromedriver.exe", chrome_options=chrome_options)
    #driver.get("https://www.google.com") #go to google.com
    #time.sleep(0.5)
    #driver.find_element_by_xpath('//*[@id="L2AGLb"]/div').click() #agree to t&c

def opennewtab(site): #open a new tab with a certian site
    global tabcount
    tabcount = tabcount + 1
    print(f"tab = {tabcount}, website = {site}")
    driver.execute_script("window.open('');") # Open a new window
    driver.switch_to.window(driver.window_handles[tabcount]) # Switch to the new window
    driver.get(site)
    
def changeoriginaltab(site): #change first tab
    driver.switch_to.window(driver.window_handles[0])
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

def fakefacebookvisit(): #fake a visit to facebook (login+interaction)
    changeoriginaltab('https://facebook.com')
    #facebooklogin() #function to log into facebook - on a bot account
    #scrollfacebook() #function to scroll facebook for 30 seconds liking a post every 10-15 seconds (scrolling at varying speeds & liking posts randomly)
    driver.close() #close tab

def fakeinstagramvisit(): #fake a visit to instagram (login+interaction)
    changeoriginaltab('https://instagram.com')
    #instagramlogin() #function to log into instagram - on a bot account
    #scrollinstagram() #function to look through first 4 people's stories (follow top 150 accounts), post a picture of a random thing (qr code for something? / computer generate content? - different every post)
    driver.close() #close tab

def faketwittervisit(): #fake a visit to twitter (login+interaction)
    changeoriginaltab('https://twitter.com')
    #twitterlogin() #function to log into twitter - on a bot account
    #scrolltwitter() #function to look & like first 4 peoples latest tweets, tweet a message (loreum ipsum? / computer generated content? - always different)
    driver.close() #close tab

def opendummysites(): #opens all dummy sites
    openbrowser() #open browser window
    fakefacebookvisit() #fake a visit to facebook
    fakeinstagramvisit() #fake a visit to instagram
    faketwittervisit() #fake a visit to twitter
    for site in dummysitelist: #for each dummysite:
        opennewtab(site) #open the dummy site in a new tab
        time.sleep(random.randint(1,6)) #spend a random amount of time (between 1 -> 6 seconds)
        driver.close() #close tab

def clickadverts():
    print("")
    #randomly choose ads to click on, click 40 -> 50% of ads on a page
    #stay on the site for a random time setting (1 -> 8 seconds)

def openadsites(): #visit & interact with sites in adsitelist
    for site in adsitelist: #do this for each site
        opennewtab(site) #open the ad page
        clickadverts() #randomly interact
        driver.close() #close tab

#########################

##Main Code:
#compareips()


#opendummysites()
#openadsites()
#########################