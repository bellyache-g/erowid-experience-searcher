# to do
# figure out why I can't .strip() the title of the report
# figure out how to write to text file

import requests
from bs4 import BeautifulSoup
import time


urlcount = 0
foundurls = 0
outfile = open('experience.txt', 'a')

# cycle through potential PHP id #'s

for i in range(900000):
    # generate links to cycle through up to 900k
    updatedurl = F"https://www.erowid.org/experiences/exp.php?ID={i}"

    # add one to urlcount variable to keep running total of how many URLs we've found
    urlcount += 1

    # let user know what number URL we're trying


    # make request and get webpage from link generator
    urlget = requests.get(updatedurl)


    urltry = urlget.text


    soup = BeautifulSoup(urltry, 'html.parser')

    # find the title with the <title> tag of the post
    title = soup.title

    #string the title

    titlestring = str(title)

    # fix the fucker
    fixedtitle1 = titlestring.replace("<title>", '')

    # fix it again
    fixedtitle2 = fixedtitle1.replace("</title>", '')

    # final fix
    fixedtitle = fixedtitle2.replace(" - Erowid Exp - ", "-")

    issomethinghere = soup.find_all("div", class_="title")

    if issomethinghere == []:
        continue
    else:
        print("found @ URL #" + str(urlcount) + " " + str(fixedtitle) + " " + updatedurl)

        #nospace = soup.text
        #reallynospace = nospace.strip()
        #print(reallynospace)
        outfile.write(str(fixedtitle) + " " + updatedurl + "\n")

#   time.sleep(.2)
