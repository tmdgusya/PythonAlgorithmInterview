import unittest


def soltion(money: int):
    MONEY_TYPES = [500, 100, 50, 10]
    answer = 0
    for coin in MONEY_TYPES:
        answer += money // coin
        money = money % coin
    return answer


class TestClass(unittest.TestCase):

    def test_one(self):
        self.assertEqual(soltion(1260), 6)
