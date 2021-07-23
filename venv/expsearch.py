import requests
from bs4 import BeautifulSoup
import time
import os


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

        nospace = soup.text
        reallynospace = nospace.strip()
        reallynospace = reallynospace.replace("[ View as PDF (for printing) ]", '')
        reallynospace = reallynospace.replace("[ View as LaTeX (for geeks) ]",'')
        reallynospace = reallynospace.replace("COPYRIGHTS: All reports are copyright Erowid and you agree not to download or analyze the report data without contacting Erowid Center and receiving permission first.", '')
        reallynospace = reallynospace.replace("""Experience Reports are the writings and opinions of the individual authors who submit them.
Some of the activities described are dangerous and/or illegal and none are recommended by Erowid Center.""", '')
        reallynospace = reallynospace.replace("""Erowid Experience Vault
© 1995-2017 Erowid""", '')
        reallynospace = os.linesep.join([s for s in reallynospace.splitlines() if s])
        reallynospace = reallynospace.replace("""More than 2 million people use Erowid every month.
During the pandemic, only 70 of those contributed $1 or more.
Donations are down significantly. Please Contribute.""", '')
        reallynospace = reallynospace.replace("""Erowid - Honest Global Drug Information
We're an educational non-profit working to provide a balanced, honest look at
psychoactive drugs and drug use--to reduce harms, improve benefits, & support
reasonable policies. This work is made possible by $10, $50, & $100 donations.""", '')
        reallynospace = reallynospace.replace("""Thinning Out Your Physical Library?
If you have books or periodicals about drugs, contribute them to Erowid!
Your old books will find a good home in our library or for a supporter. [details]""", '')
        reallynospace = reallynospace.replace("[ Switch Colors ]", '')


        print(reallynospace)
        outfile.write(str(fixedtitle) + " " + updatedurl + "\n" + reallynospace)

#   time.sleep(.2)
