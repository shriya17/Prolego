import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def fetchSquadList(col_name):
    column = browser.find_element_by_css_selector(col_name)
    col_list = column.find_elements_by_class_name("info")
    cnt = 0
    for line in col_list:
        if cnt < 12:
            print line.find_element_by_class_name("name").text + "  -  " + line.find_element_by_class_name("position").text
            cnt = cnt+1
        else:
            try:
                sub_in = line.find_element_by_css_selector(".icn.sub-on")
                if sub_in is not None:
                    print line.find_element_by_class_name("name").text + "  -  " + line.find_element_by_class_name(
                        "position").text
            except:
                continue





def getSquadUrl(fileName):
    text_write = open("MatchSquad-2013.txt",'a')
    with open(fileName,'r') as list:
        for line in list:
            try:
                browser.get("https://www.premierleague.com/match/" + line)
                tab = browser.find_element_by_class_name("matchCentreSquadLabelContainer")
                tab.click()
                time.sleep(0.1)
                fetchSquadList(".col-4-m ")
                fetchSquadList(".col-4-m.right")
            except:
                continue

browser = webdriver.Chrome()
getSquadUrl("Matches-2013.txt")