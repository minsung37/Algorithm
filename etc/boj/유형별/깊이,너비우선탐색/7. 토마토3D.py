from collections import deque
import sys
input = sys.stdin.readline

# 토마토 정보 입력받기
m, n, h = map(int, input().split())
tomato = []
for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int, input().split())))
    tomato.append(temp)

# 토마토가 익는 방향
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

# 토마토 좌표 큐에 넣기
queue = deque()
for z in range(h):
    for x in range(n):
        for y in range(m):
            if tomato[z][x][y] == 1:
                queue.append((z, x, y))

# 토마토 익히기(BFS)
while queue:
    z, x, y = queue.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if nx < 0 or ny < 0 or nz < 0 or nx >= n or ny >= m or nz >= h:
            continue
        if tomato[nz][nx][ny] == 0:
            queue.append((nz, nx, ny))
            tomato[nz][nx][ny] = tomato[z][x][y] + 1

# 정답출력
day = []
temp = []
for i in tomato:
    for j in i:
        if 0 in j:
            print(-1)
            exit(0)
        temp.append(max(j))
    day.append(max(temp))
print(max(day) - 1)