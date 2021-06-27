import unittest

class CaseOne(unittest.TestCase):

    def valid_palindrom(self, wording : str):
        strs = []
        for char in wording:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True


    def test_case_one(self):
        self.assertTrue(self.valid_palindrom("A man, a plan, a canal: Panama"))

    def test_case_two(self):
        self.assertFalse(self.valid_palindrom("race a car"))
