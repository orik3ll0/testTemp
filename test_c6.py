import requests
import re
import unittest
import pytest

class tagLower:

    def wikipedia(response, tag_name):
        contentText = response.text
        pattern = r"<{0}>(.*?)</{0}>".format(tag_name)
        reuslt = re.search(pattern, contentText)
        return reuslt.group(1).lower()


class Test_tagLower(unittest.TestCase):

    def test_errors(self):
        url = "https://en.wikipedia.org/w/index.php"
        r = requests.get(url=url)
        tag_name = 'title'

        with pytest.raises(Exception):
            self.assertNotIsInstance(r, requests.models.Response)

        with pytest.raises(Exception):
            self.assertIsNone(tag_name)

        with pytest.raises(Exception):
            self.assertNotIn(tag_name, r.text)


    def test_wikipedia(self):
        url = "https://en.wikipedia.org/w/index.php"
        r = requests.get(url=url)
        result = tagLower.wikipedia(r, 'title')
        self.assertTrue(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()