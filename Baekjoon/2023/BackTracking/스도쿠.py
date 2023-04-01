import sys
input = sys.stdin.readline
size = 9


def backTracking(depth):
    if depth == len(zero):
        for line in sudoku:
            print(*line, sep="")
        exit(0)
    x, y = zero[depth]
    check = set()
    # 가로
    for num in sudoku[x]:
        check.add(num)
    # 세로
    for row in range(size):
        check.add(sudoku[row][y])
    # 3x3
    nx, ny = (x // 3) * 3, (y // 3) * 3
    for i in range(3):
        for j in range(3):
            check.add(sudoku[nx + i][ny + j])
    for i in range(1, size + 1):
        if i not in check:
            sudoku[x][y] = i
            backTracking(depth + 1)
            sudoku[x][y] = 0


sudoku = [list(map(int, list(input().rstrip()))) for _ in range(9)]
zero = []
for i in range(size):
    for j in range(size):
        if sudoku[i][j] == 0:
            zero.append([i, j])
backTracking(0)