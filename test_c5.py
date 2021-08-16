import requests
import re
import unittest
import pytest

class tagLower:

    def wikipedia(response, tag_name):
        contentText = response.text
        pattern = r"<{0}[^>]*>(.*?)<\s*/\s*{0}>".format(tag_name)
        result = re.search(pattern, contentText)

        return print(result.group(1).lower())


class Test_tagLower(unittest.TestCase):

    def test_wikipedia(self):
        url = "https://en.wikipedia.org/w/index.php"
        r = requests.get(url=url)

        assert tagLower.wikipedia(r, 'title') is None


if __name__ == '__main__':
    unittest.main()