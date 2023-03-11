from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline


def dijkstra(start, distance):
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


n, e = map(int, input().split())
graph = defaultdict(list)

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
    graph[v].append([u, w])
a, b = map(int, input().split())

INF = int(1e9)
distance_s = [INF] * (n + 1)
distance_a_b = [INF] * (n + 1)
distance_b_a = [INF] * (n + 1)
distance_e = [INF] * (n + 1)

dijkstra(1, distance_s)
dijkstra(a, distance_a_b)
dijkstra(b, distance_b_a)
dijkstra(n, distance_e)

path1 = distance_s[a] + distance_a_b[b] + distance_e[b]
path2 = distance_s[b] + distance_b_a[a] + distance_e[a]

result = min(path1, path2)
if result >= INF:
    print(-1)
else:
    print(result)