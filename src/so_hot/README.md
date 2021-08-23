# 효율성 개선

## Solution One

- **TimeComplexity : O(n^2)**

```python
def mix(food1, food2):
    return food1 + (food2 * 2)

def solution(scoville: list, K: int):

    # 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶다.

    # TODO: 맨 앞의 원소가 스코빌 지수보다 높은 지 확인한다. 맞다면 끝낸다.
    # TODO: 배열에서 두개를 dequeue 를 이용해서 앞에서 pop 하고, 스코빌 지수 공식을 더해서 넣는다.
    # TODO: 소팅한다.
    answer = 0
    scoville.sort(reverse=True)
    while scoville[len(scoville) - 1] < K:
        if len(scoville) <= 1 :
            return -1
        first_food = scoville.pop()
        second_food = scoville.pop()

        scoville.append(mix(first_food, second_food))
        scoville.sort(reverse=True)
        answer += 1

    return answer
```

## Solution Two

- **TimeComplexity : O(nlogn)**

```python
def mix(food1, food2):
    return food1 + (food2 * 2)

def solution(scoville: list, K: int):
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
```
