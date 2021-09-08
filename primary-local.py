##Imports:
from sys import platform
import os
import time
#########################

##Definitons:


#########################

##Functions:

def  readstatus(): #get current bot status from `status.txt` file
    file = open('status.txt', "r")
    status = file.read()
    file.close()

    return status


#########################

##Main Code:

#Have a server / bot always running this code:
#setup script? / custom machine image?
#run the main bot code + make money!
#facilitate destruction of bot /server




#while True:
for i in range (10):
    if readstatus() == "Bot Not Running": #while no bot is running start a new one
        os.startfile("bot-local.py")
        time.sleep(0.5)