# https://programmers.co.kr/learn/courses/30/lessons/42626
# 더 맵게
import heapq


def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    while True:
        first = heapq.heappop(scoville)
        temp = first
        if first >= K:
            break
        count = count + 1
        second = heapq.heappop(scoville)
        first = first + 2 * second
        if temp == first:
            return - 1
        if len(scoville) == 1:
            if scoville[0] < K:
                return - 1
        heapq.heappush(scoville, first)
    return count


print(solution([1, 2, 3, 9, 10, 12], 7))