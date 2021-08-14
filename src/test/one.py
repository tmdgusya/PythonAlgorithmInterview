import unittest
from itertools import combinations

def solution(fruitWeights, k):
    result = {}
    answer = []
    finalList = []
    for i in range(0, len(fruitWeights)-(k-1)):
        tempList = []
        for j in range(k):
            tempList.append(fruitWeights[j+i])
        finalList.append(tempList)

    for i in range(len(finalList)):
        dd = 0
        for j in finalList[i]:
            dd = max(j, dd)
        result[dd] = True

    for key in result.keys():
        answer.append(key)

    answer.sort(reverse=True)

    return answer

class Unit(unittest.TestCase):

    def test_oen(self):
        self.assertEqual(solution([30, 40, 10, 20, 30], 3), [40, 30])

    def test_two(self):
        self.assertEqual(solution([10, 20, 30, 40, 50], 2), [50, 40, 30, 20])
    
    def test_thr(self):
        self.assertEqual(solution([10, 50, 20, 40, 20, 30], 3), [50, 40])