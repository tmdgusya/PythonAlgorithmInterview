import unittest

# N 이 1이 될때까지 1을 빼거나, K 로 나눈다.
# 1을 빼는 거 보다 보통 4로 나누는게 훨씬 유리하다.
# 25 // 4 = 6 
# 6 // 4 = 1
def solution(n, k):
    result = 0
    while n >= k:
        while n % k != 0:
            n = n - 1
            result += 1
        n //= k
        result += 1

    while n > 1: 
        n -= 1
        result += 1
    return result


class UnitTest(unittest.TestCase):

    def test_one(self):
        self.assertEqual(solution(25, 4), 5)
