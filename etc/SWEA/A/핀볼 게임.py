from collections import defaultdict


def search(i, j, dd):
    score = 0
    x, y, d = i, j, dd
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        # 자기 자신 자리로 돌아오면 종료
        if nx == i and ny == j:
            break
        # 외벽만나면 방향전환
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            d = (d + 2) % 4
            score = score + 1
        # 삼각형만난경우
        # 5 : 벽
        elif board[nx][ny] == 5:
            d = (d + 2) % 4
            score = score + 1
        # 1
        elif board[nx][ny] == 1:
            if d == 하 or d == 좌:
                if d == 하:
                    d = 우
                if d == 좌:
                    d = 상
            # 튕겨져나옴
            else:
                d = (d + 2) % 4
            score = score + 1
        # 2
        elif board[nx][ny] == 2:
            if d == 상 or d == 좌:
                if d == 상:
                    d = 우
                if d == 좌:
                    d = 하
            else:
                d = (d + 2) % 4
            score = score + 1
        # 3
        elif board[nx][ny] == 3:
            if d == 상 or d == 우:
                if d == 상:
                    d = 좌
                if d == 우:
                    d = 하
            else:
                d = (d + 2) % 4
            score = score + 1
        # 4
        elif board[nx][ny] == 4:
            if d == 우 or d == 하:
                if d == 하:
                    d = 좌
                if d == 우:
                    d = 상
            else:
                d = (d + 2) % 4
            score = score + 1
        # 웜홀 만난경우
        elif 5 < board[nx][ny]:
            hole0 = worm_hole[board[nx][ny]][0]
            hole1 = worm_hole[board[nx][ny]][1]
            if [nx, ny] == hole0:
                nx, ny = hole1
            else:
                nx, ny = hole0
        elif board[nx][ny] == -1:
            break
        # 자리옮기기
        x, y = nx, ny
    return score


T = int(input())
#    하  좌  상  우
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
하, 좌, 상, 우 = 0, 1, 2, 3
for t in range(T):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    # 웜홀 담기
    worm_hole = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if board[i][j] > 5:
                worm_hole[board[i][j]].append([i, j])

    result = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                for d in range(4):
                    result = max(result, search(i, j, d))
    print("#%d %d" % (t + 1, result))