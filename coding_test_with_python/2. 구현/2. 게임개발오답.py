# 크기, 좌표, 방향 입력받기
n, m = map(int, input().split())
x, y, d = map(int, input().split())

# 맵, 방향
a = []
#    북  서  남 동
di = [0, 3, 2, 1]
nx = [0, -1, 1, 0]
ny = [1, 0, -1, 0]
for i in range(n):
    line = list(map(int, input().split()))
    a.append(line)

res = 0
escape = True
while escape:
    # 북
    count = 0
    if di.index(d) == 0:
        x = x + nx[0]
        y = y + ny[0]
        if a[x][y] == 1:
            d = 3
            x = x - nx[0]
            y = y - ny[0]
        else:
            a[x - nx[0]][y - ny[0]] = 1
            res = res + 1
    # 서
    elif di.index(d) == 3:
        x = x + nx[3]
        y = y + ny[3]
        if a[x][y] == 1:
            d = 2
            x = x - nx[3]
            y = y - ny[3]
        else:
            a[x - nx[3]][y - ny[3]] = 1
            res = res + 1
    # 남
    elif di.index(d) == 2:
        x = x + nx[2]
        y = y + ny[2]
        if a[x][y] == 1:
            d = 1
            x = x - nx[2]
            y = y - ny[2]
        else:
            a[x - nx[2]][y - ny[2]] = 1
            res = res + 1
    # 동
    elif di.index(d) == 1:
        x = x + nx[1]
        y = y + ny[1]
        if a[x][y] == 1:
            d = 0
            x = x - nx[1]
            y = y - ny[1]
        else:
            a[x - nx[1]][y - ny[1]] = 1
            res = res + 1
    # 네방향 갈곳 없는경우
    for i in range(4):
        x = x + nx[i]
        y = y + ny[i]
        if a[x][y] == 1:
            count = count + 1
            x = x - nx[i]
            y = y - ny[i]
        if count == 4:
            escape = False

print(res)
