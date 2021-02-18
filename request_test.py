import requests

url = 'http://163.20.152.6/news/u_news_v2.asp?id={06F7660F-61BF-4F19-9C15-7CDA485F1814}&newsid=884&PageNo=1&skeyword='
r = requests.get(url)


# get attribute
print(r.status_code)
print(r.encoding)
print(r.apparent_encoding)
#print(r.text)
#print(r.content)

content = r.text.split('\n')
print(content[-1])

# request error
#requests.ConnectionError
#requests.HTTPError
#requests.URLRequired
#requests.TooManyRedirects
#requests.ConnectTimeout
#requests.Timeout
#r.raise_for_status()

# request package main method funtions
# request.request()
# request.get()
# request.head()
# request.post()
# request.put()
# request.patch()
# request.delete()

'''

HTTP 協議

URL format: http://host[:port][path]
host: IP address
port: default as 80
path: path of the request source

HTTP method 
GET、HEAD、POST、PUT、PATCH、DELETE

'''




