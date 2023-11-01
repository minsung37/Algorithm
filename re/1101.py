# 감시 피하기
# https://www.acmicpc.net/problem/18428
import copy
import sys
input = sys.stdin.readline


n = int(input())
board = [list(input().split()) for _ in range(n)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
answer = "NO"
teacher_list, space_list = [], []
for x in range(n):
    for y in range(n):
        if board[x][y] == "T":
            teacher_list.append([x, y])
        elif board[x][y] == "X":
            space_list.append([x, y])
max_i = len(space_list)


def recursion(depth, check_list, i):
    if depth == 3:
        check(check_list)
        return
    for idx in range(i, max_i):
        check_list.append(space_list[idx])
        recursion(depth + 1, check_list, idx + 1)
        check_list.pop()


def check(check_list):
    new_board = copy.deepcopy(board)
    for x, y in check_list:
        new_board[x][y] = "O"
    check = True
    for tx, ty in teacher_list:
        for d in range(4):
            count = 1
            while True:
                nx = tx + dx[d] * count
                ny = ty + dy[d] * count
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    break
                if new_board[nx][ny] == "O":
                    break
                if new_board[nx][ny] == "S":
                    check = False
                    break
                count = count + 1
    if check:
        print("YES")
        exit(0)


recursion(0, [], 0)
print("NO")