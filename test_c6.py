import requests
import re
import unittest
import pytest


class TagLower:

    def wikipedia(response, tag_name):
        contentText = response.text
        pattern = r"<{0}>(.*?)</{0}>".format(tag_name)
        reuslt = re.search(pattern, contentText)
        return reuslt.group(1).lower()


class TestTagLower(unittest.TestCase):

    def test_errors(self):
        url = "https://en.wikipedia.org/w/index.php"
        r = requests.get(url=url)
        tag_name = 'title'

        # checking if r is instance of requests.models.Response
        with pytest.raises(Exception):
            assert not isinstance(r, requests.models.Response)

        # checking if tag_name is instance of string
        with pytest.raises(Exception):
            assert not isinstance(tag_name, str)

        # checking if tag_name in textpip install flake8
        with pytest.raises(Exception):
            self.assertNotIn(tag_name, r.text)


if __name__ == '__main__':
    unittest.main()
