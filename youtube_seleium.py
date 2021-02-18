from selenium import webdriver
import time
import pandas as pd 
browser = webdriver.Chrome()
browser.get('https://www.youtube.com/channel/UCj_z-Zeqk8LfwVxx0MUdL-Q/videos')

for i in range(1, 10):
    browser.execute_script('var q=document.documentElement.scrollTop=5000')
    time.sleep(5)

for i in range(1, 10):
    browser.execute_script('var q=document.documentElement.scrollTop=0')
    time.sleep(1)


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

browser.get(DF.iloc[2,0])
time.sleep(5)
browser.maximize_window()
time.sleep(1)
browser.execute_script('var q=document.documentElement.scrollTop=5000')
time.sleep(20)
for i in range(1, 10):
    # scrollTop = 10000 : 向下拉
    browser.execute_script('var q=document.documentElement.scrollTop=10000')
    time.sleep(10)

#for i in range(1, 10):
#    browser.execute_script('var q=document.documentElement.scrollTop=0')
#    time.sleep(1)
browser.execute_script('var q=document.documentElement.scrollTop=200')
time.sleep(5)

names = []
comments = []
i = 1
location = 'ytd-item-section-renderer>div#contents>ytd-comment-thread-renderer:nth-child(' + str(i) + ')>ytd-comment-renderer#comment>div#body>div#main'
while (location):
    try:
        
        header_location = location + '>div#header>div#header-author>a>span'
        name = browser.find_element_by_css_selector(header_location).text
        

        comment_location = location + '>ytd-expander>div#content>yt-formatted-string:nth-child(2)'
        comment = browser.find_element_by_css_selector(comment_location).text

        names.append(name)
        comments.append(comment)

        i += 1
        location = 'ytd-item-section-renderer>div#contents>ytd-comment-thread-renderer:nth-child(' + str(i) + ')>ytd-comment-renderer#comment>div#body>div#main'

    except:
        break
df = {
    "name": names,
    "comment": comments
}

DF = pd.DataFrame(df)
print(DF)
