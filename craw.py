import datetime
from bs4 import BeautifulSoup
import requests
import urllib.request
import time



def CurrentTime():
    #Get Current Date/Time in DD-MM-YY HH:MM:SS PM/AM Format
    DateNow = datetime.datetime.now()
    DateNowFormat = DateNow.strftime("%I:%M %p %d-%m-%y")
    return DateNowFormat

def GetPrice():
    # Set the URL you want to webscrape from
    url = "https://coinmarketcap.com/currencies/bitcoin/"
    request = urllib.request.urlopen(url,data=None)
    requestHTML = request.read()
    soup = BeautifulSoup(requestHTML,features="html.parser")
    price_find = soup.find("span", class_="h2 text-semi-bold details-panel-item--price__value")
    price = price_find.string
    name_find = soup.find("h1", class_="details-panel-item--name")
    name = name_find.string
    return price , name

while True:
    respo = input("Do you want to run? \n")

    if(respo == "yes"):
        print("Script Started at " + CurrentTime())
        file = open('C:/Users/Saroosh/Desktop/test.txt','a')
        for x in range(0,1,1):
            PriceNow = GetPrice()
            TimeNow = CurrentTime()
            file.write( str(PriceNow) + ', ' + TimeNow + '\n')
            print('Price: ' + str(PriceNow) + "   Time: " +TimeNow)
            time.sleep(1)
        print("Script Finished Successfully at " + CurrentTime() )
        file.close()
        break

    elif (respo == "no"):
        print("Script Not Ran!")
        break

    else:
        print("Please enter correct response! (yes/no)")
