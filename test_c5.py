import requests
import re
import unittest
import pytest

class tagLower:

    def wikipedia(response, tag_name):
        contentText = response.text
        pattern = r"<{0}>(.*?)</{0}>".format(tag_name)
        reuslt = re.search(pattern, contentText)
        if reuslt == 'None':
            raise Exception('Result is not success')
        else:
            return print(reuslt.group(1).lower())


class Test_tagLower(unittest.TestCase):
    def test_wikipedia(self):
        url = "https://en.wikipedia.org/w/index.php"
        r = requests.get(url=url)
        with pytest.raises(Exception) as e:
            assert tagLower.wikipedia(r, 'title')
            assert str(e.value) == "Invalid tag name"
        # print(tagLower.wikipedia(r, 'footer'))
        # assert r.status_code == 200


if __name__ == '__main__':
    unittest.main()