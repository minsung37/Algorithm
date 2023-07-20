import copy
from collections import deque


def backtracking(depth, prev_board):
    global result
    if depth == n:
        # 최대한 적은 개수의 벽돌이 있어야함
        result = min(result, brick_count(prev_board))
        return

    # 각각의 벽돌깨고 탐색
    for i in range(w):
        board = copy.deepcopy(prev_board)
        next_board = drop_ball(i, board)
        backtracking(depth + 1, next_board)


def drop_ball(spot, board):
    # bfs로 벽돌제거
    queue = deque()
    for x_index in range(h):
        if board[x_index][spot] != 0:
            queue.append([x_index, spot, board[x_index][spot]])
            board[x_index][spot] = 0
            break
    while queue:
        x, y, size = queue.popleft()
        for d in range(4):
            xx, yy = x, y
            for s in range(size - 1):
                nx = xx + dx[d] * (s + 1)
                ny = yy + dy[d] * (s + 1)
                # 범위 벗어나는 경우
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    continue
                # 0 이적혀있는 칸인경우
                if board[nx][ny] == 0:
                    continue
                queue.append([nx, ny, board[nx][ny]])
                board[nx][ny] = 0

    for j in range(w):
        stack = []
        for i in range(h):
            if board[i][j] != 0:
                stack.append(board[i][j])
                board[i][j] = 0
        if not stack:
            continue
        for i in range(h - 1, -1, -1):
            board[i][j] = stack.pop()
            if not stack:
                break

    return board


def brick_count(board):
    broken_brick = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] != 0:
                broken_brick = broken_brick + 1
    return broken_brick


T = int(input())
for t in range(T):
    n, w, h = map(int, input().split())
    origin_board = [list(map(int, input().split())) for _ in range(h)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    result = int(1e9)
    backtracking(0, origin_board)
    print("#%d %d" % (t + 1, result))