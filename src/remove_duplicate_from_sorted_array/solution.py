import unittest


def solution(nums: list):
        unique = list(set(nums))
        for i, v in enumerate(unique):
            nums[i] = v
        return len(nums)

class TestClass(unittest.TestCase):

    def test_one(self):
        self.assertEqual(3, solution([1, 1, 2]))


if __name__ == '__main__':
    unittest.main()
