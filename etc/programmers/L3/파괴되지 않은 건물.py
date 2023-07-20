# https://school.programmers.co.kr/learn/courses/30/lessons/92344
# 파괴되지 않은 건물
def solution(board, skill):
    # [type, r1, c1, r2, c2, degree]
    n, m = len(board), len(board[0])
    prefix = [[0] * (m + 1) for _ in range(n + 1)]

    for types, r1, c1, r2, c2, degree in skill:
        degree = degree if types == 2 else -degree
        prefix[r1][c1] += degree
        prefix[r1][c2 + 1] -= degree
        prefix[r2 + 1][c1] -= degree
        prefix[r2 + 1][c2 + 1] += degree

    for i in range(n):
        for j in range(m):
            prefix[i][j + 1] += prefix[i][j]

    for j in range(m):
        for i in range(n):
            prefix[i + 1][j] += prefix[i][j]

    answer = 0
    for x in range(n):
        for y in range(m):
            if board[x][y] + prefix[x][y] > 0:
                answer = answer + 1

    return answer


print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
               [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]))
