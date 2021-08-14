import unittest

def solution(number: int):
    # 연산이 4가지

    # 1. X 가 5로 나누어 떨어지면, 5로 나눈다
    # 2. X 가 3으로 나누어 떨어지면, 3으로 나눈다.
    # 3. X 가 2로 나누어 떨어지면, 2로 나눈다.
    # 4. X 가 1로 나누어 떨어지면 1로 나눈다.
    # min(x/5, x/3, x/2, x-1)

    d = [0] * 30001

    for i in range(2, number + 1):

        if number % 5 == 0:
            # i 가 현재 횟수에서 1이 되는 수인데, 5로 나누는게 더 적은게 좋으므로 min 으로 비교
            d[i] = min(d[i], d[i // 5])
        
        if number % 3 == 0:
            d[i] = min(d[i], d[i // 3])

    return d[number] 


class TestClass(unittest.TestCase):
    next