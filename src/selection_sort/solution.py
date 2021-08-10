import unittest


def selection_sort(arr: list):

    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

class TestClass(unittest.TestCase):

    def test_one(self):
        arr = [1,5,3,8,4,9]
        self.assertEqual(selection_sort(arr), [1,3,4,5,8,9])
