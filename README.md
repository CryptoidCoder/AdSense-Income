# Ads - Passive Income

# THIS HAS MOVED TO A NEW REPO: [https://github.com/CryptoidCoder/Selenium-Ad-Clicker](https://github.com/CryptoidCoder/Selenium-Ad-Clicker)


## **Branches:**
### patching = the newest updates for the project
### website = the website html for running the homemade adsite
### local = a version that runs locally (not using AWS and not self replicating, etc)


<hr>

## **Basic Idea:**
Make Bots visit websites that have ads,
Those ads being viewed make me money,
The bots will then grow & scale based on how much the bots are currently earning.

<hr><br>

## **Main Explanation On How We Would Do That:**
We have two main files (`bot-manager.py` & `bot.py`);

`bot-manager.py`:
- Runs on something locally (A home lab, Raspberry Pi, etc)
- Facilitates the bots
- Runs replications (Looks at money income Vs running costs, and self scales for maximum efficency.)
- Rundown:
- - Uses the AWS SDK to create & run a `bot.py` container.
- - Does this with multiple contianers at once, therefore more ads are being viewed, therefore more money made.



`bot.py`:
- Runs in AWS (within a container)
- Does teh actual ad visiting & clicking.
- Rundown:
- - That container will cycle through Proxy servers, using each IP address only once
- - It will visit multiple ad pages on homemade sites, and multiple pre-existing ad sites.

<br>

## **Services We Would Use:**
- Netlify / Github Pages  (Making Homemade AdSites)
- AWS ECS (Running containers on)
- AWS EC2 (Running Self Replication code?)
- Google AdSense (For the actual homemade ads)
- AWS SNS (Requesting Scale-Ups Via SMS bots)



## With Thanks To:
### People Who Have Helped Me With This Project:
- [Sawyer Bristol](https://github.com/LegitCamper)
- [Jim Knowler](https://github.com/JimKnowler)
- [ITWithLyam](https://github.com/itwithlyam)
- [The HackHorsham Community](https://www.facebook.com/hackhorsham)
