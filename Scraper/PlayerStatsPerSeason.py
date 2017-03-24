import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""
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
        text_file.write(x.get_attribute("href") + "\n")

    text_file.close()
    return




# Get browser instance
browser = webdriver.Chrome()
# Function call
getClubUrl("https://www.premierleague.com/clubs/")
