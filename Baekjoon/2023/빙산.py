import sys
from collections import deque
input = sys.stdin.readline


def is_separate(sx, sy):
    queue = deque()
    queue.append([sx, sy])
    visited[sx][sy] = True
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                # 빙산이 있고 방문 안한경우
                if ice[nx][ny] != 0 and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                # 빙산 녹는 높이 저장
                elif ice[nx][ny] == 0:
                    melt[x][y] = melt[x][y] + 1


n, m = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
year, separate = 0, False
while True:
    ice_count = 0
    visited = [[False] * m for _ in range(n)]
    melt = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if ice[i][j] != 0 and not visited[i][j]:
                is_separate(i, j)
                ice_count = ice_count + 1
    # 빙산녹이기
    for i in range(n):
        for j in range(m):
            ice[i][j] = ice[i][j] - melt[i][j]
            if ice[i][j] < 0:
                ice[i][j] = 0
    if ice_count == 0:
        break
    if ice_count > 1:
        separate = True
        break
    year = year + 1
if separate:
    print(year)
else:
    print(0)