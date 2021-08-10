import requests
import re

class GetDataFromUrl:

    def tagLower(response, tag_name):
        contentText = response.text
        pattern = r"<{0}>(.*?)</{0}>".format(tag_name)
        reuslt = re.search(pattern, contentText)
        return print(reuslt.group(1).lower())

    url = "https://en.wikipedia.org/w/index.php"
    r = requests.get(url=url)

    tagLower(r, 'title')

    #better way could be with bs4
