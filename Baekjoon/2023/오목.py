import sys
input = sys.stdin.readline

size = 19
omok = [list(map(int, input().split())) for _ in range(size)]
# 하 우 우상 우하
dx, dy = [1, 0, -1, 1], [0, 1, 1, 1]
winner = []
for x in range(size):
    for y in range(size):
        if omok[x][y] != 0:
            my_stone = omok[x][y]
            for n in range(4):
                x1, y1 = x, y
                x2, y2 = x, y
                sum_stone = 1
                coordinate = [[x, y]]
                flag1 = True
                flag2 = True
                for i in range(6):
                    nx = x1 + dx[n]
                    ny = y1 + dy[n]
                    if flag1:
                        if 0 <= nx < size and 0 <= ny < size:
                            x1, y1 = nx, ny
                            if omok[x1][y1] == my_stone:
                                coordinate.append([x1, y1])
                                sum_stone = sum_stone + 1
                            else:
                                flag1 = False
                    nx = x2 - dx[n]
                    ny = y2 - dy[n]
                    if flag2:
                        if 0 <= nx < size and 0 <= ny < size:
                            x2, y2 = nx, ny
                            if omok[x2][y2] == my_stone:
                                coordinate.append([x2, y2])
                                sum_stone = sum_stone + 1
                            else:
                                flag2 = False
                if sum_stone == 5:
                    coordinate.sort(key=lambda x: (x[1], x[0]))
                    winner.append([my_stone, coordinate[0][0] + 1, coordinate[0][1] + 1])
if winner:
    print(winner[0][0])
    print(winner[0][1], winner[0][2])
else:
    print(0)