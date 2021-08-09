import unittest


def solution(arr):

    x = 0
    result = []

    for i in range(1, len(arr)):
        temp = arr[x] + arr[i]
        th_idx = -1
        for k in range(1, len(arr)):
            if k == i:
                continue
            if k == x:
                continue
            if arr[k] == temp * -1 :
                th_idx = k
        if th_idx != -1 and th_idx != x and th_idx != i:
            x += 1
            result.append([arr[x], arr[i], arr[th_idx]])
        print(result)
    return result


class TestSimple(unittest.TestCase):
    def test_one(self):
        self.assertEquals([[-1,-1,2],[-1,0,1]], solution([-1,0,1,2,-1,-4]))
