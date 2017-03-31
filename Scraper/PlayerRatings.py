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
                text_file.write(x.get_attribute("title") + "-" + str + "\n")
                #print str
                #print x.get_attribute("title")









browser = webdriver.Chrome()
getClubLinks("https://www.fifaindex.com/teams/fifa14_13/?league=13")