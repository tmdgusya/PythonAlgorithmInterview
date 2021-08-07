import unittest


def solution(list):
    
    result = 0
    for data in list:
        min_value = 100000
        for ele in data:
            min_value = min(ele, min_value)
        result = max(min_value, result)
    return result


class TestCase(unittest.TestCase):
    
    def test_one(self):
        self.assertEqual(solution([[3,1,2],[4,1,4],[2,2,2]]), 2)