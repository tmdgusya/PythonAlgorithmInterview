import unittest
from typing import List

'''
이전의 y 축 최고점 ~ 만큼 채운다.

0일 경우는 이전꺼로 채운다.
'''


def two_pointer(height: List[int]):
    # TODO List 가 없을때는 0을 리턴한다.
    if not height:
        return 0

    # TODO 물의 초기 용량을 정한다.
    water = 0

    # TODO Two Pointer 방식이므로, 왼쪽 오른쪽을 초기화 한다.
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    # TODO 결국 작은 쪽이 큰쪽으로 오면서 이동해야 물이 항상 채워질것이다.
    while left < right:

        left_max, right_max = max(left_max, height[left]), max(right_max, height[right])

        if left_max < right_max:
            water += left_max - height[left]
            left += 1
        else:
            water += right_max - height[right]
            right -= 1

    return water


def stack_solution(height: List[int]):
    if not height:
        return 0

    stack = []
    water = 0

    for i in range(len(height)):

        while stack and height[i] > height[stack[-1]]:
            value = stack.pop()

            if not len(stack):
                break

            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]] - height[value])

            water += distance * waters

        stack.append(i)

    return water


class TestClass(unittest.TestCase):

    def test_case_one(self):
        self.assertEqual(two_pointer([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)

    def test_case_two(self):
        self.assertEqual(stack_solution([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)
