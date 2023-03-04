import sys
input = sys.stdin.readline


def backtraking(index, office):
    global result
    if index == depth:
        # 0의 최대개수 카운팅
        count = 0
        for i in range(n):
            for j in range(m):
                if office[i][j] == 0:
                    count = count + 1
        result = min(result, count)
        return
    num, x, y = cctvs[index]
    if num == 1:
        for d in range(4):
            watch_list = []
            xx, yy = x, y
            while True:
                nx = xx + dx[d]
                ny = yy + dy[d]
                if 0 <= nx < n and 0 <= ny < m:
                    # 벽이 아니면
                    if office[nx][ny] != 6:
                        xx, yy = nx, ny
                        watch_list.append([xx, yy])
                    # 벽인경우
                    else:
                        break
                else:
                    break
            for wx, wy in watch_list:
                if office[wx][wy] == 0:
                    office[wx][wy] = chr(index)
            backtraking(index + 1, office)
            for wx, wy in watch_list:
                if office[wx][wy] == chr(index):
                    office[wx][wy] = 0
    elif num == 2:
        select = 0
        for _ in range(2):
            watch_list = []
            xx, yy = x, y
            select = (select + 1) % 4
            for _ in range(2):
                xxx, yyy = xx, yy
                select = (select + 2) % 4
                while True:
                    nx = xxx + dx[select]
                    ny = yyy + dy[select]
                    if 0 <= nx < n and 0 <= ny < m:
                        # 벽이 아니면
                        if office[nx][ny] != 6:
                            xxx, yyy = nx, ny
                            watch_list.append([xxx, yyy])
                        # 벽인경우
                        else:
                            break
                    else:
                        break
            for wx, wy in watch_list:
                if office[wx][wy] == 0:
                    office[wx][wy] = chr(index)
            backtraking(index + 1, office)
            for wx, wy in watch_list:
                if office[wx][wy] == chr(index):
                    office[wx][wy] = 0
    elif num == 3:
        select = 0
        for _ in range(4):
            watch_list = []
            xx, yy = x, y
            select = (select + 1) % 4
            for _ in range(2):
                xxx, yyy = xx, yy
                select = (select + 1) % 4
                while True:
                    nx = xxx + dx[select]
                    ny = yyy + dy[select]
                    if 0 <= nx < n and 0 <= ny < m:
                        # 벽이 아니면
                        if office[nx][ny] != 6:
                            xxx, yyy = nx, ny
                            watch_list.append([xxx, yyy])
                        # 벽인경우
                        else:
                            break
                    else:
                        break
            for wx, wy in watch_list:
                if office[wx][wy] == 0:
                    office[wx][wy] = chr(index)
            backtraking(index + 1, office)
            for wx, wy in watch_list:
                if office[wx][wy] == chr(index):
                    office[wx][wy] = 0
    elif num == 4:
        not_select = 0
        for _ in range(4):
            watch_list = []
            xx, yy = x, y
            not_select = (not_select + 1) % 4
            for d in range(4):
                xxx, yyy = xx, yy
                if d == not_select:
                    continue
                while True:
                    nx = xxx + dx[d]
                    ny = yyy + dy[d]
                    if 0 <= nx < n and 0 <= ny < m:
                        # 벽이 아니면
                        if office[nx][ny] != 6:
                            xxx, yyy = nx, ny
                            watch_list.append([xxx, yyy])
                        # 벽인경우
                        else:
                            break
                    else:
                        break
            for wx, wy in watch_list:
                if office[wx][wy] == 0:
                    office[wx][wy] = chr(index)
            backtraking(index + 1, office)
            for wx, wy in watch_list:
                if office[wx][wy] == chr(index):
                    office[wx][wy] = 0
    elif num == 5:
        watch_list = []
        for d in range(4):
            xx, yy = x, y
            while True:
                nx = xx + dx[d]
                ny = yy + dy[d]
                if 0 <= nx < n and 0 <= ny < m:
                    # 벽이 아니면
                    if office[nx][ny] != 6:
                        xx, yy = nx, ny
                        watch_list.append([xx, yy])
                    # 벽인경우
                    else:
                        break
                else:
                    break
        for wx, wy in watch_list:
            if office[wx][wy] == 0:
                office[wx][wy] = chr(index)
        backtraking(index + 1, office)
        for wx, wy in watch_list:
            if office[wx][wy] == chr(index):
                office[wx][wy] = 0


n, m = map(int, input().split())
office_origin = [list(map(int, input().split())) for _ in range(n)]
# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cctvs = []
for i in range(n):
    for j in range(m):
        if 1 <= office_origin[i][j] <= 5:
            cctvs.append([office_origin[i][j], i, j])
depth, result = len(cctvs), int(1e9)
backtraking(0, office_origin)
print(result)