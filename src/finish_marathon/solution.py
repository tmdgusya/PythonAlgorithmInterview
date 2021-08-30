import unittest


def solution(participant, completion):
    
    # sort alphabet
    participant.sort()
    completion.sort()

    print(participant)
    print(completion)

    # find user who completed marathon from completion array
    left = 0
    right = 0
    answer = 0
    while left < len(participant):
        if participant[left] == completion[right]:
            left += 1
            if right < len(completion)-1:
                right += 1
        else:
            answer = left
            left += 1

    return participant[answer]



    
        

class TestClass(unittest.TestCase):

    def test_one(self):
        self.assertEqual(solution(["leo", "kiki", "eden"], ["eden", "kiki"]), "leo")

    def test_two(self):
        self.assertEqual(solution(['ana', 'mislav', 'mislav', 'stanko'], ['ana', 'mislav', 'stanko']), "mislav")
