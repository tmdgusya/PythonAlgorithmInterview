import unittest

def solution(s: str):
    
    word_hash = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10
    }

    for i in word_hash.keys():
        start_point = s.find(i)
        if start_point != -1:
            s = s.replace(i, str(word_hash[i]))

    return int(s)

class TestClass(unittest.TestCase):

    def test_solution_one(self):
        self.assertEqual(solution("one4seveneight"), 1478)
