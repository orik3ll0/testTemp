import requests
import re

class GetDataFromUrl:

    def tagLower(response, tag_name):
        contentText = response.text
        pattern = r"<{0}[^>]*>(.*?)<\s*/\s*{0}>".format(tag_name)
        result = re.search(pattern, contentText)
        return print(result.group(1).lower())

    url = "https://en.wikipedia.org/w/index.php"
    r = requests.get(url="https://en.wikipedia.org/w/index.php")

    tagLower(r, 'title')

    #better way could be with bs4
