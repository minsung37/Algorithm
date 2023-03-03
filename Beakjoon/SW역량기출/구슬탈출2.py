from collections import deque
import sys
input = sys.stdin.readline


def move(x, y, d):
    count1 = 0
    # 갈곳이 벽이거나, 지금 구멍이면 탈출
    while board[x + dx[d]][y + dy[d]] != '#' and board[x][y] != "O":
        x = x + dx[d]
        y = y + dy[d]
        count1 = count1 + 1
    return x, y, count1


n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# red, blue, hole 찾기
rx, ry, bx, by = 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if board[i][j] == "R":
            rx, ry = i, j
        if board[i][j] == "B":
            bx, by = i, j
queue = deque()
queue.append([rx, ry, bx, by, 1])
count = 0
while queue:
    rx, ry, bx, by, count = queue.popleft()
    visited = [[rx, ry, bx, by]]
    if count > 10:
        print(-1)
        exit(0)
    for d in range(4):
        rnx, rny, r_count = move(rx, ry, d)
        bnx, bny, b_count = move(bx, by, d)
        # 둘다 구멍에 빠진경우
        if board[rnx][rny] == board[bnx][bny] == "O":
            continue
        # 빨강만 구멍에 빠진경우
        if board[rnx][rny] == "O":
            print(count)
            exit(0)
        # 겹친 경우 => 많이 이동한애 뒤로한칸
        if rnx == bnx and rny == bny:
            if r_count < b_count:
                bnx = bnx - dx[d]
                bny = bny - dy[d]
            else:
                rnx = rnx - dx[d]
                rny = rny - dy[d]
        next_turn = [rnx, rny, bnx, bny]
        if next_turn not in visited:
            visited.append(next_turn)
            queue.append([rnx, rny, bnx, bny, count + 1])
print(-1)