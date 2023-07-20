import sys

# 스도쿠 입력받기
sudoku = []
for i in range(9):
    sudoku.append(list(map(int, sys.stdin.readline().split())))

# 0 인것의 좌표 target에 저장하기
target = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            target.append([i, j])

# 0인 좌표의개수
k = len(target)
for i in range(k):

    # 0에 들어갈 후보군
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = set(a)

    # 0에 못들어가는 숫자
    b = set()
    x = target[i][0]
    y = target[i][1]

    # 가로 세로 검사
    for j in range(9):
        temp = sudoku[x][j]
        b.add(temp)
        temp = sudoku[j][y]
        b.add(temp)

    # 네모칸검사
    nx = (x // 3) * 3
    ny = (y // 3) * 3
    for p in range(3):
        for q in range(3):
            temp = sudoku[nx + p][ny + q]
            b.add(temp)
    c = a - b
    sudoku[x][y] = c.pop()

for i in range(9):
    print(*sudoku[i])
