import heapq
import sys
input = sys.stdin.readline


def topology_sort():
    heap = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            heapq.heappush(heap, i)
    while heap:
        x = heapq.heappop(heap)
        result.append(x)
        for next in graph[x]:
            indegree[next] = indegree[next] - 1
            if indegree[next] == 0:
                heapq.heappush(heap, next)


n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    prev, curr = map(int, input().split())
    indegree[curr] = indegree[curr] + 1
    graph[prev].append(curr)
result = []
topology_sort()
print(*result)