import re
import unittest


def is_palindrom(wording: str):
    wording = wording.lower()

    wording = re.sub('[^a-z0-9]', '', wording)

    return wording == wording[::-1]


class CaseThr(unittest.TestCase):

    def test_case_one(self):
        self.assertTrue(is_palindrom("A man, a plan, a canal: Panama"))

    def test_case_two(self):
        self.assertFalse(is_palindrom("race a car"))
