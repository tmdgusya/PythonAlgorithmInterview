import unittest


def solution(arr: list, m, k):
    arr.sort(reverse=True)

    bigger_one = arr[0]
    bigger_two = 0

    result = 0

    if len(arr) > 1:
        bigger_two = arr[1]

    while m > 0:
        m -= 1
        for i in range(k):
            m -= 1
            result += bigger_one
        result += bigger_two
    
    return result

def solution_by_math(arr:list, m, k):
    arr.sort(reverse=True)

    bigger_one = arr[0]
    bigger_two = 0

    if len(arr) > 1:
        bigger_two = arr[1]

    result = 0

    # 수열을 그려보면 큰수가 더해지는 건 (M//(K+1)) * k 
    # 근데 M 이 K+1 보다 작을 수도 있으므로 M % (K+1)

    count = m // (k + 1) * k
    count += m % (k + 1)

    result += bigger_one * count
    result += (m - count) * bigger_two

    return result

    


class TestClass(unittest.TestCase):

    def test_one(self):
        self.assertEqual(solution([2,4,5,4,6], 8, 3), 46)

    def test_two(self):
        self.assertEqual(solution_by_math([2,4,5,4,6], 8, 3), 46)