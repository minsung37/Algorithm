from collections import deque
import sys
input = sys.stdin.readline

# 토마토가 익는 방향
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 토마토정보 입력받기
tomato = []
m, n = map(int, input().split())
for i in range(n):
    tomato.append(list(map(int, input().split())))

# 토마토가 있는 좌표를 큐에 넣기
queue = deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append((i, j))

# 토마토 익히기(BFS)
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if tomato[nx][ny] == -1:
            continue
        if tomato[nx][ny] == 0:
            tomato[nx][ny] = tomato[x][y] + 1
            queue.append((nx, ny))

# 정답출력
day = []
for i in tomato:
    if 0 in i:
        print(-1)
        exit(0)
    day.append(max(i))
print(max(day) - 1)