import unittest


def dictionary_search(arr: list, target: int):
    dict = {}
    for i, ele in enumerate(arr):
        dict[ele] = i

    for i, ele in enumerate(arr):
        if target - ele in dict and i != dict[target - ele]:
            return [i, dict[target - ele]]


class TestClass(unittest.TestCase):

    def test_case_one(self):
        self.assertEqual(dictionary_search([2, 7, 11, 15], 9), [0, 1])

    def test_case_two(self):
        self.assertEqual(dictionary_search([3, 2, 4], 6), [1, 2])

    def test_case_thr(self):
        self.assertEqual(dictionary_search([3, 3], 6), [0, 1])

    def test_case_four(self):
        self.assertEqual(dictionary_search([3, 2, 3], 6), [0, 2])
