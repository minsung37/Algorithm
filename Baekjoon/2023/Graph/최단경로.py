from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline


def dijkstra(start):
    queue = []
    heapq.heappush(queue, [0, start])
    distance[start] = 0
    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node] < dist:
            continue
        for next_node in graph[node]:
            cost = dist + next_node[1]
            if cost < distance[next_node[0]]:
                distance[next_node[0]] = cost
                heapq.heappush(queue, [cost, next_node[0]])


# 정점의 개수, 간선의 개수
V, E = map(int, input().split())
k = int(input())
graph = defaultdict(list)

# u에서 v로 가는 가중치 w인 간선이 존재한다
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

# 최단거리 테이블
INF = int(1e9)
distance = [INF] * (V + 1)

dijkstra(k)
for node in range(1, V + 1):
    if distance[node] == INF:
        print("INF")
    else:
        print(distance[node])