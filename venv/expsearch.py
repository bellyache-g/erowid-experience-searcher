import requests
from bs4 import BeautifulSoup
import time
import csv
import random

# iterate through possible php ids

urlcount = 0

for i in range(900000):
    updatedurl = F'https://www.erowid.org/experiences/exp.php?ID={i}'
    urlcount += 1
    print('trying URL ' + str(urlcount) + ' is something here?')
    urlget = requests.get(updatedurl)
    urltry = urlget.content
    soup = BeautifulSoup(urltry, 'html.parser')
    issomethinghere = soup.find_all("div", class_="title")
    if issomethinghere == []:
        print('no')
    else:
        print('yes: ' + str(issomethinghere))
        print(updatedurl)
#       craziness = soup.find('body')
#       print(craziness)

    #time.sleep(.2)


