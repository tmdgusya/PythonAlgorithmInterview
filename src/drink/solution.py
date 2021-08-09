import unittest
from collections import deque

# 음료수 얼려먹기 dfs
def solution_dfs(m, n, graph):

    def dfs(x,y):

        if x <= -1 or x >= m or y <= -1 or y >= n:
            return False
        
        if graph[x][y] == 0:
            # visited => True
            graph[x][y] = 1

            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
            return True
        return False
    
    result = 0

    for i in range(m):
        for j in range(n):
            if dfs(x=i, y=j) == True:
                result +=1

    return result

# 음료수 얼려먹기 bfs
def solution_bfs(m, n, graph):

    x_ = [0,0,1,-1]
    y_ = [1,-1,0,0]
    visited = [[False for i in range(n)] for j in range(m)]


    def bfs(x,y):
        queue = deque([x,y])
        visited[x][y] = True
        while queue:
            z = queue.popleft()
            k = queue.popleft()
            for i in range(len(x_)):
                dx = x_[i] + z
                dy = y_[i] + k

                if dx >= 0 and dx < m and dy >= 0 and dy < n and graph[dx][dy] == 0:
                    if visited[dx][dy] != True:
                        visited[dx][dy] = True
                        queue.append(dx)
                        queue.append(dy)
        return True

    result = 0

    for i in range(m):
        for j in range(n):
            if visited[i][j] != True and graph[i][j] != 1:
                if bfs(i,j) == True:
                    result += 1
    
    return result;

    
class UnitTest(unittest.TestCase):
    
    def test_case_one(self):
        graph = [[0,0,1,1,0],[0,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0]]
        self.assertEqual(solution_dfs(4, 5, graph=graph), 3)

    def test_case_two(self):
        graph = [[0,0,1,1,0],[0,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0]]
        self.assertEqual(solution_bfs(4, 5, graph=graph),3);