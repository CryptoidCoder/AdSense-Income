##Imports:
from sys import platform
import os
import time
import sys
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


try: #make sre it has astatus.txt to start with
    file = open("status.txt")
    file.read()
    file.close()
except:
    file = open("status.txt", "w")
    file.write("Bot Not Running")

while True:
    if os.path.exists('exit'):
        os.remove('exit')
        sys.exit()
    else:
        print("No Exit File exists, carrying on.... \n")
        if readstatus() == "Bot Not Running": #while no bot is running start a new one
            os.system("python bot-local.py")
            time.sleep(0.5)