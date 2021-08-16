import unittest

def solution(n: int):
    
    dp = [0] * n;

    dp[0] = 1
    dp[1] = 3

    for i in range(2, n):
        dp[i] = dp[i-1] + 2 * dp[i-2];

    return dp[n-1];


class TestClass(unittest.TestCase):
    
    def test_one(self):
        self.assertEqual(solution(3), 5);