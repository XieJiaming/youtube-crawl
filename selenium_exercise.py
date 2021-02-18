from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time
# 開啟google網頁
browser = webdriver.Chrome('/Users/jiamingxie/bin/chromedriver')
browser.get('http://google.com/')
time.sleep(3)
# 找尋輸入欄，輸入'youtube'並送出
element = browser.find_element_by_name('q')
element.send_keys('youtube')
element.submit()
time.sleep(3)
# 找到需求網頁並點擊
# browser.find_element_by_class_name('LC20lb DKV0Md').click()
browser.find_element(By.XPATH, '//span[text()="YouTube"]').click()

# 找尋輸入欄，並輸入'上班不要看'
# element = browser.find_element_by_id('search')
element = browser.find_element(By.XPATH, "//input[@id='search']")
element.send_keys('蔡阿嘎')
browser.find_element_by_id('search-icon-legacy').click()
time.sleep(1)
# 找到需求網頁並點擊
browser.find_element_by_css_selector('div#info>ytd-channel-name').click()
time.sleep(1)

# 切換至影片列，為了能夠把所有影片找出來
wait = WebDriverWait(browser, 10)
wait.until(lambda  browser: browser.find_element_by_css_selector('div#tabsContent>paper-tab:nth-child(4)>div'))
browser.find_element_by_css_selector('div#tabsContent>paper-tab:nth-child(4)>div').click()

# 網頁下拉，讓影片慢慢吐出來
for i in range(1, 5):
    browser.execute_script('var q=document.documentElement.scrollTop=5000')
    time.sleep(3)

hrefs = []
titles = []
i = 1
location = 'div#items>ytd-grid-video-renderer:nth-child(' + str(i) + ')>div#dismissable>div#details>div#meta>h3>a#video-title'
while (location):
    try:
    
        urls = browser.find_element_by_css_selector(location)

        hrefs.append(urls.get_attribute("href"))
        titles.append(urls.get_attribute("title"))
#        print(urls.get_attribute("href"))
#        print(urls.get_attribute("title"))
#        print(urls.get_attribute("aria-label"))

        i += 1
        location = 'div#items>ytd-grid-video-renderer:nth-child(' + str(i) + ')>div#dismissable>div#details>div#meta>h3>a#video-title'
    except:
        break
df = {"href": hrefs,
      "title": titles
     }
DF = pd.DataFrame(df)
print(DF)
time.sleep(5)