import unittest
from typing import List


def all_search(nums: list, target: int) -> List:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            sum = nums[i] + nums[j]
            if sum == target:
                return [i, j]


class TestClass(unittest.TestCase):

    def test_case_one(self):
        self.assertEqual(get_answer([2, 7, 11, 15], 9), [0, 1])

    def test_case_two(self):
        self.assertEqual(get_answer([3, 2, 4], 6), [1, 2])

    def test_case_thr(self):
        self.assertEqual(get_answer([3, 3], 6), [0, 1])

    def test_case_four(self):
        self.assertEqual(get_answer([3, 2, 3], 6), [0, 2])
