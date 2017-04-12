import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""
    _author_ = "Shriya Mishra"

    Script Description

"""

def fetchSquadList(col_name,text_file):
    time.sleep(0.3)
    column = browser.find_element_by_css_selector(col_name)
    col_header = column.find_element_by_class_name("position")
    text_file.write("*************** " + col_header.text + "*****************\n")
    col_list = column.find_elements_by_class_name("info")
    cnt = 0
    for line in col_list:
        if cnt < 12:
            try:
                sub_out = line.find_element_by_css_selector(".icn.sub-off")
                text_file.write(line.find_element_by_class_name("name").text + "  -  " + line.find_element_by_class_name(
                        "position").text + " so" + '\n')

                cnt += 1
            except:
                text_file.write(line.find_element_by_class_name("name").text + "  -  " + line.find_element_by_class_name(
                    "position").text + '\n')
                cnt += 1

        else:
            try:
                sub_in = line.find_element_by_css_selector(".icn.sub-on")
                if sub_in is not None:
                    text_file.write(line.find_element_by_class_name("name").text + "  -  " + line.find_element_by_class_name(
                        "position").text+" si " + '\n')
            except:
                print "Fetch failed Sub-on"





def getSquadUrl(fileName):
    text_file = open("MatchSquad-2013.txt",'w')
    with open(fileName,'r') as list:
        for line in list:
            try:
                browser.get("https://www.premierleague.com/match/" + line)
                tab = browser.find_element_by_class_name("matchCentreSquadLabelContainer")
                tab.click()
                time.sleep(0.3)
                fetchSquadList(".col-4-m ",text_file)
                fetchSquadList(".col-4-m.right",text_file)
            except:
                continue

browser = webdriver.Chrome()
getSquadUrl("Matches-2013.txt")