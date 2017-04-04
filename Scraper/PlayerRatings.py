import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""

    Script Description:
    This python script fetches each premier league player's EA Sports FIFA ratings for all seasons
    from 2013 onwards. The script scrapes data from the site www.fifaindex.com. The task is achieved by
    performing two tasks - fetching each club's url from the season page & then fetching player ratings
    for each player in the club page.


"""


def getClubLinks(url):
    """

    :param url: string
    :return: none

    This function parses the url, fetches the club url links from the page and stores
    them in a text file. First, we find elements using an id.

    """
    text_file = open("FIFA_Club_Links-2013.txt","w")
    browser.get(url)
    time.sleep(0.5)
    table = browser.find_element_by_id("no-more-tables")
    names = table.find_elements_by_tag_name("a")
    items = set()
    for x in names:
        str = x.get_attribute("href")
        if "https://www.fifaindex.com/team/" in str:
            if str not in items:
                items.add(str)
                text_file.write(x.get_attribute("title") + "," + str + "\n")
                #print str
                #print x.get_attribute("title")



def getPlayerRatings(fileName):
    text_file = open("PlayerRatings-2013.txt","w")
    with open(fileName,"r") as ins:
        for line in ins:
            str1 = line.split(',')
            browser.get(str1[1])
            time.sleep(0.1)
            table = browser.find_element_by_id("no-more-tables")
            body = table.find_element_by_tag_name("tbody")
            rows = body.find_elements_by_tag_name("tr")
            for x in rows:
                data = x.find_elements_by_tag_name("td")
                name = ''.encode('utf-8')
                name = name.encode('utf-8')
                position = ''.encode('utf-8')
                rating = ''.encode('utf-8')
                for y in data:
                    str2 = y.get_attribute("data-title")
                    if str2 == "Name":
                        name = y.text.encode('utf-8')
                        #text_file.write(y.text.encode('utf-8') + " ")
                    elif str2 == "OVR / POT":
                        #text_file.write(y.text.encode('utf-8') + " ")
                        position = y.text.encode('utf-8')
                    elif str2 == "Preferred Positions":
                        rating = y.text.encode('utf-8')
                        #rating = rating[:2]
                        #text_file.write(y.text.encode('utf-8') + "\n")

                text_file.write(str1[0] + ',' + name + ',' + position + ',' + rating[:2] + '\n')

    text_file.close()


def cleanRating(fileName):
    text_file = open("PlayerRatings-2013-Final.txt","w")
    with open(fileName,"r+") as ins:
        for line in ins:
            str1 = line.split(',')
            rating = str1[2]
            temp = rating
            rating = rating[:2]
            text_file.write(line.replace(temp,rating))




browser = webdriver.Chrome()
#getClubLinks("https://www.fifaindex.com/teams/fifa14_13/?league=13")
getPlayerRatings("FIFA_Club_Links-2013.txt")
cleanRating("PlayerRatings-2013.txt")