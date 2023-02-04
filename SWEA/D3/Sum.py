# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13_BWKACUCFAYh
# 1209. [S/W 문제해결 기본] 2일차 - Sum
for _ in range(10):
    n = input()
    matrix, check = [], []
    left, right = 0, 0
    x, y = 0, 99
    for _ in range(100):
        temp = list(map(int, input().split()))
        matrix.append(temp)

    # 가로
    for row in matrix:
        check.append(sum(row))

    # 세로
    for col in range(100):
        temp = []
        for k in range(100):
            temp.append(matrix[k][col])
        check.append(sum(temp))

    # 우하 방향대각선
    for k in range(100):
        left = left + matrix[k][k]
    check.append(left)

    # 좌하 방향 대각선
    for _ in range(100):
        right = right + matrix[x][y]
        x = x + 1
        y = y - 1
    check.append(right)

    print("#" + n, max(check))