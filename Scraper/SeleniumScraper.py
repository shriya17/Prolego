import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://www.premierleague.com/results?co=1&se=22&cl=-1")
time.sleep(2)

elem = browser.find_element_by_tag_name("body")

no_of_pagedowns = 50

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    no_of_pagedowns-=1

post_elems = browser.find_elements_by_class_name("matchList")
text_file = open("Output.txt", "w")
for post in post_elems:
    text_file.write(post.text + "\n")
text_file.close()