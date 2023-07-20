# [1차] 프렌즈4블록
# https://school.programmers.co.kr/learn/courses/30/lessons/17679
def solution(m, n, board):

    for i in range(len(board)):
        board[i] = list(board[i])

    # 블럭 4개 없애기
    def boom(board):
        boom_list = []
        for x in range(m - 1):
            for y in range(n - 1):
                if board[x][y] == board[x + 1][y] == board[x][y + 1] == board[x + 1][y + 1] != "0":
                    boom_list.append([x, y])
                    boom_list.append([x + 1, y])
                    boom_list.append([x, y + 1])
                    boom_list.append([x + 1, y + 1])
        if len(boom_list) == 0:
            return True
        for x, y in boom_list:
            board[x][y] = "0"

    # 블럭 내리기
    def down(board):
        check = False
        for x in range(m - 1):
            for y in range(n):
                if board[x + 1][y] == "0" and board[x][y] != "0":
                    board[x + 1][y], board[x][y] = board[x][y], board[x + 1][y]
                    check = True
        return check

    # 블럭 없애고 내리고 반복
    while True:
        if boom(board):
            break
        while True:
            if not down(board):
                break

    count = 0
    for x in range(m):
        for y in range(n):
            if board[x][y] == "0":
                count = count + 1
    return count


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
print(solution(8, 5, ['HGNHU', 'CRSHV', 'UKHVL', 'MJHQB', 'GSHOT', 'MQMJJ', 'AGJKK', 'QULKK']))
print(solution(5, 6, ['AAAAAA','BBAATB','BBAATB','JJJTAA','JJJTAA']))