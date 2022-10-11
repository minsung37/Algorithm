# 합승 택시 요금
# https://school.programmers.co.kr/learn/courses/30/lessons/72413
import heapq


def solution(n, s, a, b, fares):
    mx = int(1e9)

    graph = [[] for _ in range(n + 1)]
    distance_x = [mx] * (n + 1)
    distance_a = [mx] * (n + 1)
    distance_b = [mx] * (n + 1)

    for p, q, cost in fares:
        graph[p].append((q, cost))
        graph[q].append((p, cost))

    def dijkstra(s, distance):
        q = []
        heapq.heappush(q, (0, s))
        distance[s] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    dijkstra(s, distance_x)
    result = [0] * (n + 1)

    for i in range(1, n + 1):
        dijkstra(i, distance_a)
        dijkstra(i, distance_b)
        result[i] = distance_a[a] + distance_b[b] + distance_x[i]
        distance_a = [mx] * (n + 1)
        distance_b = [mx] * (n + 1)

    return min(result[1:])


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))