from collections import defaultdict
from collections import deque
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = [0] * n
for i in range(1, n + 1):
    temp = 0
    for j in range(1, n + 1):
        if i == j:
            continue
        queue = deque()
        visited = [False] * (n + 1)
        queue.append([i, 0])
        visited[i] = True
        while queue:
            x, count = queue.popleft()
            if x == j:
                temp = temp + count
                break
            for k in graph[x]:
                if not visited[k]:
                    visited[k] = True
                    queue.append([k, count + 1])
    result[i - 1] = temp

target = min(result)
for idx, count in enumerate(result):
    if count == target:
        print(idx + 1)
        break
