from collections import deque
import sys
input = sys.stdin.readline


def bfs(sx, sy):
    size = 1
    queue = deque()
    queue.append([sx, sy])
    drawing[sx][sy] = 0
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if drawing[nx][ny] == 1:
                    drawing[nx][ny] = 0
                    size = size + 1
                    queue.append([nx, ny])
    return size


n, m = map(int, input().split())
drawing = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = []
for i in range(n):
    for j in range(m):
        if drawing[i][j] == 1:
            result.append(bfs(i, j))

if result:
    print(len(result))
    print(max(result))
else:
    print(0)
    print(0)
