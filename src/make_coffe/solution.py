import unittest

# 커피 기계를 size 만큼 동시에 만들 수 있을때 먼져나오는 숫자들 기입

def solution(arr: list, size):
    result = []

    while(len(result) != len(arr)):
        for i in range(size):
            arr[i] -= 1
            if(arr[i] == 0):
                result.append(i+1)
                if(size < len(arr)):
                    size += 1
            
        
    return result


class TestClass(unittest.TestCase):

    def test_one(self):
        self.assertEqual(solution([4,2,2,3,1],3), [2,3,5,1,4])

    def test_two(self):
        self.assertEqual(solution([100,1,50,1,100],1), [1,2,3,4,5])