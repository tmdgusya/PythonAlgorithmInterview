import unittest
import collections
from typing import Deque


def deq_valid_palindrom(wording: str):

    strs: Deque = collections.deque()

    for char in wording:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


class CaseTwo(unittest.TestCase):

    def test_deq_valid(self):
        self.assertTrue(deq_valid_palindrom("A man, a plan, a canal: Panama"))

    def test_deq_valid_one(self):
        self.assertFalse(deq_valid_palindrom("race a car"))
