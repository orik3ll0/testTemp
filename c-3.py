import requests

url = "https://en.wikipedia.org/w/index.php"
r = requests.get(url=url)

# for response
print(r)

# for content
print(r.text)
