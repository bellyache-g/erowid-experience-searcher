import requests
from bs4 import BeautifulSoup
import time
import csv

# iterate through possible php ids

urlcount = 0

for i in range(900000):
    updatedurl = F'https://www.erowid.org/experiences/exp.php?ID={i}'
    print(updatedurl)
    urlcount += 1
    print('This is URL ' + str(urlcount) + ' is something here?')
    urlget = requests.get(updatedurl)
    urltry = urlget.content
    soup = BeautifulSoup(urltry, 'html.parser')
    issomethinghere = soup.find_all("div", class_="title")
    if issomethinghere == []:
        print('nothing is here')
    else:
        print('something is here: ' + str(issomethinghere))
    #time.sleep(.2)


