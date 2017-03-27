import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""
    _author_ = "Sourabh Swain"
    Script Description:

    This python script is used to fetch player stats from every premier league club for every season
    from 2013-14 onwards. To get all the player stats, we distribute the overall task into the following
    sub-tasks:

    1. Fetching the URLs for all premier league clubs for every season.
    2. Accessing the squad list for every club and going to every player's stats page.
    3. Fetching the actual stats for the player and writing them onto a text file in a formatted manner.

"""

def getClubUrl(url):

    """
        Function Definition:
        Name: getClubUrl
        Arguments:
            Name: url
            Type: string
        Returns: None

        Function Description:
        The function goes through the url for a premier league season and fetches all the
        premier league clubs url for the same season. The urls are then written onto a text file for further use.

    """

    browser.get(url) # Opens the url in the browser
    tiles = browser.find_element_by_class_name("indexSection")  # Finds class named indexSection
    links = tiles.find_elements_by_tag_name("li")   # Finds all the tags named li under indexSection class
    text_file = open("Club-Links.txt", "w") # Opens a text file in write mode

    # For loop with iterator named link
    for link in links:
        # Finds anchor tag for every li tag
        x = link.find_element_by_tag_name("a")
        # Writes to the text file by getting href attribute of anchor tag
        str = x.get_attribute("href")
        str = str.replace("overview", "squad")
        text_file.write(str + "\n")

    text_file.close()
    return


def getPlayerUrl(fileName):

    """

    Function Definition:
        Name: getPlayerUrl
        Arguments:
            Name: fileName
            Type: string
        Returns: None

    Function Description:
        This function goes through the links of all clubs (Club-Links.txt) and extracts the links for
        all the players from the squads page of the respective club.

    """

    text_file = open("Player-Links-2013.txt","w")
    with open(fileName, "r") as ins:
        for line in ins:
            browser.get(line)
            elem = browser.find_elements_by_xpath("//a[@class='playerOverviewCard active']")
            # players = elem.find_elements_by_tag_name("li")
            time.sleep(2)
            for player in elem:
                # link = player.find_element_by_tag_name("a")
                str = player.get_attribute("href")
                str = str.replace("overview", "squad")
                text_file.write(str + "\n")
                time.sleep(0.1)
            text_file.write("\n")

    return



# Get browser instance
browser = webdriver.Chrome()
# Function call
getClubUrl("https://www.premierleague.com/clubs/")
getPlayerUrl('Club-Links.txt')
