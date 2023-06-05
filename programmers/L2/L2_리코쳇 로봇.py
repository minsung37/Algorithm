# 리코쳇 로봇
# https://school.programmers.co.kr/learn/courses/30/lessons/169199
from collections import deque


def solution(board):
    n, m = len(board), len(board[0])
    sx, sy, tx, ty = 0, 0, 0, 0
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                sx, sy = i, j
            if board[i][j] == "G":
                tx, ty = i, j

    visited = [[int(1e9)] * m for _ in range(n)]
    visited[sx][sy] = 0

    queue = deque()
    queue.append([sx, sy])
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            xx, yy = x, y
            while True:
                nx = xx + dx[d]
                ny = yy + dy[d]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    break
                if board[nx][ny] == "D":
                    break
                xx, yy = nx, ny
            if visited[x][y] + 1 < visited[xx][yy]:
                visited[xx][yy] = visited[x][y] + 1
                queue.append([xx, yy])
    if visited[tx][ty] == int(1e9):
        return -1
    return visited[tx][ty]


print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
print(solution([".D.R", "....", ".G..", "...D"]))