from collections import deque
import sys
input = sys.stdin.readline


def bfs(i, j, color):
    queue = deque()
    queue.append([i, j])
    visited[i][j] = True
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == color and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append([nx, ny])


n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
visited = [[False] * n for _ in range(n)]
count, count_red_green = 0, 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            count = count + 1
            bfs(i, j, graph[i][j])

for i in range(n):
    for j in range(n):
        if graph[i][j] == "G":
            graph[i][j] = "R"

visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            count_red_green = count_red_green + 1
            bfs(i, j, graph[i][j])

print(count, count_red_green)
