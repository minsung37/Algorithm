# 배달
# https://school.programmers.co.kr/learn/courses/30/lessons/12978
import heapq


def solution(N, road, K):
    mx = int(1e9)
    graph = [[] for _ in range(N + 1)]
    distance = [mx] * (N + 1)

    # a에서 b로 가는 비용 graph에 저장
    for info in road:
        a, b, cost = info
        graph[a].append((b, cost))
        graph[b].append((a, cost))

    heap = []
    heapq.heappush(heap, (0, 1))
    distance[1] = 0
    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for target, money in graph[now]:
            cost = dist + money
            if cost < distance[target]:
                distance[target] = cost
                heapq.heappush(heap, (cost, target))
    count = 0
    for i in distance:
        if i <= K:
            count = count + 1
    return count


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))
