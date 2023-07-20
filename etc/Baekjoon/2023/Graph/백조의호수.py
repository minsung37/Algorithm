from collections import deque
import sys
input = sys.stdin.readline


def melt():
    k = len(melt_q)
    for _ in range(k):
        x, y = melt_q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if ground[nx][ny] == "X":
                melt_q.append([nx, ny])
                ground[nx][ny] = "."


def move():
    while swan_q:
        x, y = swan_q.popleft()
        if x == swan_list[1][0] and y == swan_list[1][1]:
            return True
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if visited[nx][ny]:
                continue
            if ground[nx][ny] == ".":
                swan_q.append([nx, ny])
            else:
                swan_q_next.append([nx, ny])
            visited[nx][ny] = True
    while swan_q_next:
        swan_q.append(swan_q_next.popleft())


r, c = map(int, input().split())
ground = [list(input().rstrip()) for _ in range(r)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
swan_list, melt_q, swan_q, swan_q_next = [], deque(), deque(), deque()
for i in range(r):
    for j in range(c):
        if ground[i][j] == "L":
            swan_list.append([i, j])
            ground[i][j] = "."
            melt_q.append([i, j])
        elif ground[i][j] == ".":
            melt_q.append([i, j])
swan_q.append(swan_list[0])
visited = [[False] * c for _ in range(r)]
first_swan = swan_list[0]
visited[first_swan[0]][first_swan[1]] = True

time = 0
while True:
    melt()
    time = time + 1
    if move():
        break
print(time)