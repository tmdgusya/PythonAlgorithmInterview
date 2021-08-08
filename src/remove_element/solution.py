import unittest


def removeElement(nums, val):
    for i in range(len(nums)):
        if nums[i] == val:
            nums[i] = -1
    
    nums.sort()
    
    count = nums.count(-1)
    
    for i in range(count):
        nums.pop(0)  

    return len(nums) - count


class TestClass(unittest.TestCase):

    def test_one(self):
        self.assertEqual(removeElement([3,2,2,3], 3), 2)