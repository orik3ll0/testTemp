import requests
import re


class GetDataFromUrl:

    def tag_Lower(response, tag_name):
        content_text = response.text
        pattern = r"<{0}[^>]*>(.*?)<\s*/\s*{0}>".format(tag_name)
        result = re.search(pattern, content_text)
        return print(result.group(1).lower())

    url = "https://en.wikipedia.org/w/index.php"
    r = requests.get(url="https://en.wikipedia.org/w/index.php")

    tag_Lower(r, 'title')
