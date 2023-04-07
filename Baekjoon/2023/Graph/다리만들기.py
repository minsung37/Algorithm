from collections import deque
from collections import defaultdict
import sys
input = sys.stdin.readline


def bfs(i, j, mark):
    queue = deque()
    queue.append([i, j])
    ground[i][j] = mark
    while queue:
        x, y = queue.popleft()
        island_info[mark].append([x, y])
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if ground[nx][ny] > 1:
                continue
            if ground[nx][ny] == 1:
                ground[nx][ny] = mark
                queue.append([nx, ny])


def find_length(start):
    global result
    queue = deque()
    for x, y in island_info[start]:
        queue.append([x, y, 0])
    visited = [[False] * n for _ in range(n)]
    while queue:
        x, y, length = queue.popleft()
        visited[x][y] = True
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if ground[nx][ny] == start:
                continue
            if visited[nx][ny]:
                continue
            if ground[nx][ny] == 0:
                if length < result:
                    visited[nx][ny] = True
                    queue.append([nx, ny, length + 1])
            if ground[nx][ny] != 0:
                result = min(result, length)
                return


n = int(input())
ground = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

mark = 2
island_info = defaultdict(list)
for i in range(n):
    for j in range(n):
        if ground[i][j] == 1:
            bfs(i, j, mark)
            mark = mark + 1

result = int(1e9)
for i in range(2, mark):
    find_length(i)
print(result)