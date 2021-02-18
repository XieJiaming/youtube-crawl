from selenium import webdriver
import time
import pandas as pd 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome('/Users/jiamingxie/bin/chromedriver') 
browser.get('https://www.youtube.com/watch?v=EgvYRVB_PJs')
browser.maximize_window()
time.sleep(1)
browser.execute_script('var q=document.documentElement.scrollTop=5000')
time.sleep(5)
for i in range(1, 10):
    browser.execute_script('var q=document.documentElement.scrollTop=5000')
    time.sleep(1)

for i in range(1, 10):
    browser.execute_script('var q=document.documentElement.scrollTop=0')
    time.sleep(1)
browser.execute_script('var q=document.documentElement.scrollTop=200')
time.sleep(5)

i = 1
location = 'ytd-item-section-renderer>div#contents>ytd-comment-thread-renderer:nth-child(' + str(i) + ')>ytd-comment-renderer#comment>div#body>div#main'


header_location = location + '>div#header>div#header-author>a>span'

name = browser.find_element_by_css_selector(header_location).text

comment_location = location + '>ytd-expander>div#content>yt-formatted-string:nth-child(2)'

comment = browser.find_element_by_css_selector(comment_location).text

print(name)
print(comment)



