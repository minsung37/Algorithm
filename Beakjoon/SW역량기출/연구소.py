import copy
from collections import deque


def backTracking(count):
    if count == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                backTracking(count + 1)
                graph[i][j] = 0


def bfs():
    global result
    graph_copy = copy.deepcopy(graph)
    queue = deque()
    for i in virus:
        queue.append(i)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph_copy[nx][ny] == 0:
                    graph_copy[nx][ny] = 2
                    queue.append([nx, ny])
    viris_count = 0
    for i in range(n):
        for j in range(m):
            if graph_copy[i][j] == 0:
                viris_count = viris_count + 1
    result = max(result, viris_count)


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
virus = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus.append([i, j])
result = 0
backTracking(0)
print(result)