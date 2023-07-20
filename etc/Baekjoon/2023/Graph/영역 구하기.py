from collections import deque
import sys
input = sys.stdin.readline


def bfs(sx, sy):
    queue = deque()
    queue.append([sx, sy])
    graph[sx][sy] = 1
    size = 0
    while queue:
        x, y = queue.popleft()
        graph[x][y] = 1
        size = size + 1
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                continue
            queue.append([nx, ny])
            graph[nx][ny] = 1
    return size


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n, m, k = map(int, input().split())
graph = [[0] * m for i in range(n)]
# 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과 오른쪽 위 꼭짓점의 x, y좌표값이
for _ in range(k):
    ldx, ldy, rux, ruy = list(map(int, input().split()))
    for x in range(ldx, rux):
        for y in range(ldy, ruy):
            graph[y][x] = 1
result = []
for x in range(n):
    for y in range(m):
        if graph[x][y] == 0:
            result.append(bfs(x, y))
result.sort()
print(len(result))
print(*result)