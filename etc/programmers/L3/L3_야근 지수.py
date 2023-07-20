# 야근 지수
# https://school.programmers.co.kr/learn/courses/30/lessons/12927
import heapq


def solution(n, works):
    for idx, work in enumerate(works):
        works[idx] = -work
    heapq.heapify(works)

    while True:
        k = -heapq.heappop(works)
        if k == 0:
            break
        k = k - 1
        n = n - 1
        heapq.heappush(works, -k)
        if n == 0:
            break

    result = 0
    for i in works:
        result = result + i ** 2
    return result


print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1, 1]))