import requests
from bs4 import BeautifulSoup

resp = requests.get('http://jwlin.github.io/py-scraping-analysis-book/ch2/blog/blog.html')

soup = BeautifulSoup(resp.text, 'html.parser')

titles = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

for title in titles:
    print(title.text.strip())


titles = soup.find_all(['p'])

for title in titles:
    print(title.text.strip())


titles = soup.find_all(['img'])

for title in titles:
    print(title)

import re 
for title in soup.find_all(re.compile('h[1-6]')):
    print(title.text.strip())

for img in soup.find_all('img', {'src': re.compile('\.png$')}):
    print(img['src'])
    
for title in soup.find_all("meta", {'content': re.compile('')}):
    print(title)

for title in soup.find_all("meta", {'content': re.compile('')}):
    print(title)

for title in soup.find_all("meta"):
    print(title)

for title in soup.find_all('img', {'src': re.compile('beginner.*\.png$')}):
    print(title['src'])

for title in soup.find_all("meta", {'content': re.compile('w')}):
    print(title)

bb = (soup.find_all('div', 'content'))
for b in bb:
    #print(b.a.text.strip())
    #print(b.text.strip())
    print([s for s in b.stripped_strings])

print(soup.find_all('div','content'))

resp = requests.get('http://blog.castman.net/py-scraping-analysis-book/ch2/table/table.html')
soup = BeautifulSoup(resp.text, 'html.parser')

prices = []

rows = soup.find('table', 'table').tbody.find_all('tr')
for row in rows:
    price = row.find_all('td')[2].text
    prices.append(int(price))

print(sum(prices)/len(prices))

links = soup.find_all('a')
for link in links:
    price = link.parent.previous_sibling.text
    prices.append(int(price))
    
print(sum(prices)/len(prices))

rows = soup.find('table', 'table').tbody.find_all('tr')
for row in rows:
#    all_tds = row.find_all('td')
    all_tds = [td for td in row.children]
    if  'href' in all_tds[3].a.attrs:
        href = all_tds[3].a['href']
    else:
        href = None
    print(all_tds[0].text, all_tds[1].text, all_tds[2].text, href, all_tds[3].a.img['src'])
    

rows = soup.find('table', 'table').tbody.find_all('tr')
for row in rows:
#    all_tds = row.find_all('td')
    all_tds = [td for td in row.children]
    print(all_tds[3].a['href'])


rows = soup.find('table', 'table').tbody.find_all('tr')
print(rows[0])


