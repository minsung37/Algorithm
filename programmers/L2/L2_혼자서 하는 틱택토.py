# 혼자서 하는 틱택토
# https://school.programmers.co.kr/learn/courses/30/lessons/160585
def solution(board):

    def same_check(board):
        is_same = True
        for x in range(3):
            for y in range(3):
                if board[x][y] != origin[x][y]:
                    is_same = False
        return is_same

    def finish_check(board):
        for x in range(3):
            o_count, x_count = 0, 0
            for y in range(3):
                if board[x][y] == 'O':
                    o_count = o_count + 1
                if board[x][y] == 'X':
                    x_count = x_count + 1
            if o_count == 3 or x_count == 3:
                return True

        for x in range(3):
            o_count, x_count = 0, 0
            for y in range(3):
                if board[y][x] == 'O':
                    o_count = o_count + 1
                if board[y][x] == 'X':
                    x_count = x_count + 1
            if o_count == 3 or x_count == 3:
                return True

        o_count, x_count = 0, 0
        for x in range(3):
            if board[x][2 - x] == 'O':
                o_count = o_count + 1
            if board[x][2 - x] == 'X':
                x_count = x_count + 1
        if o_count == 3 or x_count == 3:
            return True

        o_count, x_count = 0, 0
        for x in range(3):
            if board[x][x] == 'O':
                o_count = o_count + 1
            if board[x][x] == 'X':
                x_count = x_count + 1
        if o_count == 3 or x_count == 3:
            return True

        return False

    def backtracking(board, order):
        nonlocal result
        if same_check(board):
            result = 1
            return
        if finish_check(board):
            return
        for x in range(3):
            for y in range(3):
                if board[x][y] == '.':
                    if order % 2 == 1:
                        board[x][y] = 'O'
                    else:
                        board[x][y] = 'X'
                    backtracking(board, order + 1)
                    board[x][y] = '.'

    origin, init = [], [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    for i in board:
        origin.append(list(i))
    result = 0
    backtracking(init, 1)
    return result


print(solution(["O.X", ".O.", "..X"]))
print(solution(["OOO", "...", "XXX"]))
print(solution(["...", ".X.", "..."]))
print(solution(["...", "...", "..."]))