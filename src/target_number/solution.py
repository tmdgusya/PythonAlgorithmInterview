import unittest
from collections import deque

def solution(numbers, target):
    result = 0
    def dfs(number, depth):
        nonlocal result
        
        if depth == len(numbers):
            if number == target:
                result += 1
            return

        signed = [-number, number]
        if depth == 1:
            for i in range(len(signed)):
                dfs(signed[i] + numbers[depth], depth + 1)
                dfs(signed[i] - numbers[depth], depth+1)
        else:
            dfs(number + numbers[depth], depth + 1)
            dfs(number - numbers[depth], depth + 1)
    
    dfs(numbers[0], 1)
    return result

def solution_bfs(numbers, target):
    result = 0
    queue = deque([(0,0)]) # number, depth
    while queue:
        num, depth = queue.popleft()
        
        if depth > len(numbers):
            break
        elif depth == len(numbers) and num == target:
            result += 1
        queue.append((num + numbers[depth-1], depth+1))
        queue.append((num - numbers[depth-1], depth+1))
    return result
    



class TestCase(unittest.TestCase):
    
    def test_one(self):
        self.assertEqual(solution([1,1,1,1,1], 3), 5)

    
    def test_solution_bfs(self):
        self.assertEqual(solution_bfs([1,1,1,1,1], 3), 5)