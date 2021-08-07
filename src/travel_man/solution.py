import unittest


def solution(n :int, plans: list):
    
    x,y = 1,1

    dx = [0,0,1,-1]
    dy = [-1,1,0,0]
    move_type = ['L', 'R', 'U', 'D']

    for plan in plans:
        for i in range(len(move_type)):
            if plan == move_type[i]:
                dx = x + dx[i]
                dy = y + dy[i]
            
            # 1 <= dx < n , 1 <= dy < n
            if dx >= 1 and dy >= 1 and dx < n and dy < n:
                x, y = dx, dy
    
    return x, y



class TestClass(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution(5, ['R', 'R', 'R', 'U', 'D', 'D']), [3, 4])
