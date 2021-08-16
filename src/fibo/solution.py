import unittest


def default_fibo(x: int):
    if x == 1 or x == 2:
        return 1;
    return default_fibo(x-1) + default_fibo(x-2)


def fibo_wrapper(x):
    d = [0] * 100
    def fibo(x):
        if x == 1 or x == 2:
            return 1



class TestClass(unittest.TestCase):

    def test_one(self):
        self.assertEqual(default_fibo(4), 3)