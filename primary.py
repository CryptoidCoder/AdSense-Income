##Imports:
from sys import platform

#########################

##Definitons:


#########################

##Functions:

#Install Functions
def checkos(): #return what os the system is
    if platform == "linux" or platform == "linux2":
        # linux
        os = 'linux'
    elif platform == "darwin":
        os = 'mac'
    elif platform == "win32":
        os = 'windows'

    return os

'''
def installs(): #?????
    os = checkos()
    if os == 'linux':
        try:
            os.system("apt install snap")
            os.system("sudo snap install bw")

        except:
            os.system("apt-get install snap")
            os.system("sudo snap install bw")


    elif os == 'mac':
        try:
            os.system("brew install bitwarden-cli")

        except:
            print("Homebrew installation of bitwarden cli didnt work")

    elif os == 'windows':
        try:
            os.system("powershell")
            os.system("Set-ExecutionPolicy AllSigned")
            os.system("Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))")
            os.system("choco install bitwarden-cli")

        except:
            print("Need to try to download the executeable and execute it via cli")
'''


#########################

##Main Code:

#Have a server / bot always running this code:
#setup script? / custom machine image?


#create bot (cloud provider CLI / API)
#start bot (cloud provider CLI / API)
#install everything(python,bw-cli,git)
#get secrets from bw-cli
#git clone this repo
#run the main bot code + make money!
#facilitate destruction of bot /server