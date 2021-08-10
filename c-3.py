import requests

url = "https://en.wikipedia.org/w/index.php"

r = requests.get(url=url)
print(r)        #for response
print(r.text)   #for content
