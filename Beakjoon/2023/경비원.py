from collections import deque
import sys
input = sys.stdin.readline


def convert_coordinate(direction, spot):
    x, y = 0, 0
    # 1북 2남 3서 4동
    if direction == 1:
        x, y = 0, spot
    elif direction == 2:
        x, y = h, spot
    elif direction == 3:
        x, y = spot, 0
    elif direction == 4:
        x, y = spot, w
    return [x, y]


def bfs(sx, sy, target_x, target_y):
    visited = [[False] * (w + 1) for _ in range(h + 1)]
    queue = deque()
    visited[sx][sy] = True
    queue.append([sx, sy, 0])
    while queue:
        x, y, count = queue.popleft()
        if x == target_x and y == target_y:
            return count
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 벗어난경우
            if 0 > nx or nx >= h + 1 or 0 > ny or ny >= w + 1:
                continue
            # 길이 아닌경우
            if not load[nx][ny]:
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx, ny, count + 1])


w, h = map(int, input().split())
n = int(input())
stores = [list(map(int, input().split())) for _ in range(n)]
x, y = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
load = [[True] * (w + 1) for _ in range(h + 1)]
for i in range(1, h):
    for j in range(1, w):
        load[i][j] = False
for idx, value in enumerate(stores):
    stores[idx] = convert_coordinate(value[0], value[1])
x, y = convert_coordinate(x, y)
result = 0
for store_x, store_y in stores:
    result = result + bfs(x, y, store_x, store_y)
print(result)
