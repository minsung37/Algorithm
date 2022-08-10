# https://programmers.co.kr/learn/courses/30/lessons/42627
# 디스크 컨트롤러
import heapq


def solution(jobs):
    time, running_time, disk_count = 0, 0, 0
    n, start_time = len(jobs), -1
    for i in range(n):
        jobs[i] = list(reversed(jobs[i]))
    heap = []
    while disk_count < n:
        for i in jobs:
            if start_time < i[1] <= running_time:
                heapq.heappush(heap, i)
        if len(heap) > 0:
            curr = heapq.heappop(heap)
            start_time = running_time
            running_time = running_time + curr[0]
            time = time + (running_time - curr[1])
            disk_count = disk_count + 1
        else:
            running_time = running_time + 1
    return time // n


print(solution([[0, 3], [1, 9], [2, 6]]))