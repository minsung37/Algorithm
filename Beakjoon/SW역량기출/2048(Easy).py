import sys
input = sys.stdin.readline


def move(d, depth, board):
    global result
    if depth == 5:
        for i in board:
            result = max(result, max(i))
        return
    # 상
    new_board = [[0] * n for _ in range(n)]
    if d == 0:
        for x in range(n):
            stack = []
            for y in range(n):
                if board[y][x] != 0:
                    stack.append(board[y][x])
            for index in range(len(stack) - 1):
                if stack[index] == stack[index + 1]:
                    stack[index] = 2 * stack[index]
                    stack[index + 1] = 0
            index = 0
            for value in stack:
                if value != 0:
                    new_board[index][x] = value
                    index = index + 1
    # 하
    elif d == 1:
        for x in range(n):
            stack = []
            for y in range(n - 1, -1, -1):
                if board[y][x] != 0:
                    stack.append(board[y][x])
            for index in range(len(stack) - 1):
                if stack[index] == stack[index + 1]:
                    stack[index] = 2 * stack[index]
                    stack[index + 1] = 0
            index = 0
            for value in stack:
                if value != 0:
                    new_board[(n - 1) - index][x] = value
                    index = index + 1
    # 좌
    elif d == 2:
        for x in range(n):
            stack = []
            for y in range(n):
                if board[x][y] != 0:
                    stack.append(board[x][y])
            for index in range(len(stack) - 1):
                if stack[index] == stack[index + 1]:
                    stack[index] = 2 * stack[index]
                    stack[index + 1] = 0
            index = 0
            for value in stack:
                if value != 0:
                    new_board[index][x] = value
                    index = index + 1
    # 우
    elif d == 3:
        for x in range(n):
            stack = []
            for y in range(n - 1, -1, -1):
                if board[x][y] != 0:
                    stack.append(board[x][y])
            for index in range(len(stack) - 1):
                if stack[index] == stack[index + 1]:
                    stack[index] = 2 * stack[index]
                    stack[index + 1] = 0
            index = 0
            for value in stack:
                if value != 0:
                    new_board[(n - 1) - index][x] = value
                    index = index + 1
    # 사방 탐색
    for directiom in range(4):
        move(directiom, depth + 1, new_board)


n = int(input())
board_original = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0
for i in range(4):
    move(i, 0, board_original)
print(result)