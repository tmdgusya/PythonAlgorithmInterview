import unittest

# O(n) TimeComplexity
def selection_sort(arr: list):

    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

# O(n) TimeComplexity
def insertion_sort(arr: list):

    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr

def quick_sort(arr: list, start, end):

    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:

        # left 가 pivot 보다 큰값 찾기
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end) 

    return arr
    

class TestClass(unittest.TestCase):

    def test_one(self):
        arr = [1,5,3,8,4,9]
        self.assertEqual(selection_sort(arr), [1,3,4,5,8,9])

    def test_insertion_sort(self):
        arr = [1,5,3,8,4,9]
        self.assertEqual(insertion_sort(arr), [1,3,4,5,8,9])

    def test_quick_sort(self):
        arr = [1,5,3,8,4,9]
        self.assertEqual(quick_sort(arr=arr, start=0, end=len(arr) - 1), [1,3,4,5,8,9])
