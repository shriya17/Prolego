import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
text_file = open("Stats.txt","w")

with open("Matches.txt", "r") as ins:
    for line in ins:
        browser.get("https://www.premierleague.com/match/" + line)
        elem = browser.find_element_by_tag_name("body")
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        try:
            tab = browser.find_element_by_class_name("tablist")
            stats = tab.find_element_by_xpath(".//li[not(@class)]")
            stats.click()
            #print stats.text
            #for tab in tabs:
            #    print tab.text
            #    if tab.text == "Stats":
            #        print "Hello"
            #        tab.click()

            time.sleep(1)
            stats = browser.find_element_by_class_name("matchCentreStatsContainer")
        except:
            text_file.write("Match: " + line)
            for x in range(0, 10):
                text_file.write("XX-XX-XX-XX-XX-XX\n")
            text_file.write("Match: " + line)
            text_file.write(stats.text + "\n\n")

            text_file.write("\n\n")

