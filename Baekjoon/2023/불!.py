from collections import deque
import sys
input = sys.stdin.readline


def fire():
    for _ in range(len(fire_queue)):
        x, y = fire_queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < r and 0 <= ny < c:
                if room[nx][ny] == ".":
                    room[nx][ny] = "F"
                    fire_queue.append([nx, ny])


def escape():
    for _ in range(len(escape_queue)):
        x, y = escape_queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 > nx or nx >= r or 0 > ny or ny >= c:
                return 1
            if room[nx][ny] == "." and not visited[nx][ny]:
                visited[nx][ny] = True
                escape_queue.append([nx, ny])
    if not escape_queue:
        return 2


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
r, c = map(int, input().split())
room = [list(input().rstrip()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
fire_queue = deque()
escape_queue = deque()
for i in range(r):
    for j in range(c):
        if room[i][j] == "F":
            fire_queue.append([i, j])
        if room[i][j] == "J":
            escape_queue.append([i, j])
            room[i][j] = "."
count = 0
while True:
    count = count + 1
    fire()
    is_escape = escape()
    if is_escape == 2:
        print("IMPOSSIBLE")
        break
    if is_escape == 1:
        print(count)
        break