# 디펜스 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/142085
import heapq


def solution(n, k, enemy):
    heap = []
    result = len(enemy)
    for index, value in enumerate(enemy):
        if n < value:
            if k <= 0:
                result = index
                break
            if heap:
                temp = -heapq.heappop(heap)
                if temp > value:
                    n = n + temp - value
                    heapq.heappush(heap, -value)
                else:
                    heapq.heappush(heap, -temp)
            k = k - 1
        else:
            n = n - value
            heapq.heappush(heap, -value)
    return result


print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
print(solution(2, 4, [3, 3, 3, 3]))