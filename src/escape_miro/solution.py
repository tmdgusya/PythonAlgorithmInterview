from datetime import MINYEAR
import unittest
from collections import deque

def solution(m, n, miro):
    
    x_ = [0,0,1,-1]
    y_ = [1,-1,0,0]

    def bfs(x, y):
        # 길을 찾을때 가중치를 더하면서 간다. 해당 노드에 +1 을 더하면서 간다. 근데 처음밟는 노드가 아니면 무시한다. (가중치가 더해진 노드)
        queue = deque([x,y])

        while queue:
            
            k = queue.popleft()
            z = queue.popleft()
            for i in range(len(x_)):
                dx = k + x_[i]
                dy = z + y_[i]

                if dx < 0 or dx >= m or dy < 0 or dy >= n:
                    continue

                if miro[dx][dy] == 0:
                    continue

                if miro[dx][dy] == 1:
                    miro[dx][dy] = miro[k][z] + 1
                    queue.append(dx)
                    queue.append(dy)

        return miro[m-1][n-1]

    return bfs(0,0)

    

    
                    
            
            



class TeseClass(unittest.TestCase):

    def test_one(self):
        graph = [[1,0,1,0,1,0],[1,1,1,1,1,1],[0,0,0,0,0,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]
        self.assertEqual(solution(5, 6, miro=graph), 10)