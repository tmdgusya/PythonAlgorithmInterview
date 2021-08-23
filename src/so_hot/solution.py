import unittest
import heapq

def mix(food1, food2):
    return food1 + (food2 * 2)

def solution(scoville: list, K: int):
    
    # 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶다.
    
    # TODO: 맨 앞의 원소가 스코빌 지수보다 높은 지 확인한다. 맞다면 끝낸다.
    # TODO: 배열에서 두개를 dequeue 를 이용해서 앞에서 pop 하고, 스코빌 지수 공식을 더해서 넣는다.
    # TODO: 소팅한다.
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) <= 1 :
            return -1
        print(scoville)
        first_food = heapq.heappop(scoville)
        second_food = heapq.heappop(scoville)

        heapq.heappush(scoville, mix(first_food, second_food))
        answer += 1

    return answer


class TestClass(unittest.TestCase):

    def test_one(self):
        self.assertEqual(solution([1, 2, 3, 9, 10, 12], 7), 2)
