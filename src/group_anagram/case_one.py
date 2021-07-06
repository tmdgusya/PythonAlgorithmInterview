import unittest
import collections


def is_anagram(str):
    anagram = collections.defaultdict(list)

    for word in str:
        anagram["".join(sorted(word))].append(word)

    return list(anagram.values())


class CaseOne(unittest.TestCase):

    def test_case_one(self):
        self.assertEqual(is_anagram(["eat", "ate", "tan", "tea", "net", "bat"]), [['eat', 'ate', 'tea'], ['tan'], ['net'], ['bat']])
