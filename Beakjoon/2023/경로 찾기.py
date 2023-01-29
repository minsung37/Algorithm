from collections import defaultdict
from collections import deque
import sys
input = sys.stdin.readline


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dic = defaultdict(list)
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dic[i].append(j)

result = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        visited = [False] * n
        queue = deque()
        queue.append(i)
        check = False
        while queue:
            now = queue.popleft()
            if now == j and check:
                result[i][j] = 1
                break
            for v in dic[now]:
                if not visited[v]:
                    check = True
                    visited[v] = True
                    queue.append(v)
for i in result:
    print(*i)