import unittest


# (ON^2) but use CPython Method
def smart_search(arr: list, target: int):
    for i, ele in enumerate(arr):
        value = target - ele
        if value in arr[i + 1:]:
            return [i, arr[i + 1:].index(value) + (i + 1)]
    return 0


class TestClass(unittest.TestCase):

    def test_case_one(self):
        self.assertEqual(smart_search([2, 7, 11, 15], 9), [0, 1])

    def test_case_two(self):
        self.assertEqual(smart_search([3, 2, 4], 6), [1, 2])

    def test_case_thr(self):
        self.assertEqual(smart_search([3, 3], 6), [0, 1])

    def test_case_four(self):
        self.assertEqual(smart_search([3, 2, 3], 6), [0, 2])
