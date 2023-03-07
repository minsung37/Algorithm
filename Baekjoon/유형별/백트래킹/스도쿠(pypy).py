import sys
sudoku = []
zero = []

for i in range(9):
    sudoku.append(list(map(int, sys.stdin.readline().rstrip().split())))
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zero.append([i, j])


# 가로 검사
def check_row(x, target):
    for i in range(9):
        if sudoku[x][i] == target:
            return False
    return True


# 세로 검사
def check_col(y, target):
    for i in range(9):
        if sudoku[i][y] == target:
            return False
    return True


# 3x3박스 검사
def check_box(x, y, target):
    nx = (x // 3) * 3
    ny = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[nx + i][ny + j] == target:
                return False
    return True


# 스도쿠 채우기
def sol(k):
    # 0 전부 채워진경우
    if k == len(zero):
        for i in range(9):
            print(*sudoku[i])
        exit(0)
    # 가로, 세로, 박스에 대해서 1~9까지 검사
    for i in range(1, 10):
        x = zero[k][0]
        y = zero[k][1]
        # 들어갈수 있는경우
        if check_row(x, i) and check_col(y, i) and check_box(x, y, i):
            # 대입하고 다시실행
            sudoku[x][y] = i
            sol(k + 1)
            sudoku[x][y] = 0


sol(0)