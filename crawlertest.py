from selenium import webdriver
browser = webdriver.Chrome(executable_path='"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"')
browser.get("http://www.webbotsspidersscreenscrapers.com/hello_world.html") 
#browser.get('https://www.youtube.com/channel/UCGPlcnciT5KXLgVjLumGQgQ/videos')
print(browser.name)

