import unittest


# O(N) Time Complexity
def sequential_search(target, arr: list):
    for i in range(len(arr)):
        if arr[i] == target:
            return i + 1


def binary_search(target, arr: list, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(target, arr, start, mid - 1)
    else:
        return binary_search(target, arr, mid+1, end)



class TestClass(unittest.TestCase):

    def test_sequential_search(self):
        self.assertEqual(sequential_search('Dongbin', ['Haneul', 'Jonggu', 'Dongbin', 'Taell', 'Sangwook']), 3)

    def test_binary_search(self):
        array = [0,2,4,6,8,10,12,14,16,18]
        self.assertEqual(binary_search(4, array, 0, len(array)), 2)
