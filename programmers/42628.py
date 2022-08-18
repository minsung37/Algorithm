# https://school.programmers.co.kr/learn/courses/30/lessons/42628
# 이중우선순위큐
import heapq


def solution(operations):
    heap = []

    def convert(x):
        return int(x) + 100000000000

    def reverse(x):
        return int(x) - 100000000000

    for i in operations:
        operation = i.split()
        if operation[0] == "I":
            heapq.heappush(heap, convert(operation[1]))
        if operation[0] == "D":
            if len(heap) == 0:
                continue
            # 최대값 pop
            if operation[1] == "1":
                for j in range(len(heap)):
                    heap[j] = -heap[j]
                heapq.heapify(heap)
                heapq.heappop(heap)
                for j in range(len(heap)):
                    heap[j] = -heap[j]
                heapq.heapify(heap)
            # 최소값 pop
            else:
                heapq.heappop(heap)
    if len(heap) == 0:
        return [0, 0]
    else:
        return [reverse(max(heap)), reverse(min(heap))]


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))