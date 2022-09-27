# 행렬 테두리 회전하기
# https://school.programmers.co.kr/learn/courses/30/lessons/77485
def solution(rows, columns, queries):
    # 행렬 만들기
    matrix, count = [[0] * columns for _ in range(rows)], 1
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = count
            count = count + 1

    # 행렬 회전
    coordinate, value, result = [], [], []
    for query in queries:
        start_row, start_col, end_row, end_col = query
        x, y = start_row - 1, start_col - 1
        coordinate.append([x, y])
        value.append(matrix[x][y])
        for _ in range(end_col - start_col):
            y = y + 1
            coordinate.append([x, y])
            value.append(matrix[x][y])
        for _ in range(end_row - start_row):
            x = x + 1
            coordinate.append([x, y])
            value.append(matrix[x][y])
        for _ in range(end_col - start_col):
            y = y - 1
            coordinate.append([x, y])
            value.append(matrix[x][y])
        for _ in range(end_row - start_row):
            x = x - 1
            coordinate.append([x, y])
            value.append(matrix[x][y])
        coordinate.pop(0)
        value.pop()
        for i in range(len(value)):
            matrix[coordinate[i][0]][coordinate[i][1]] = value[i]
        result.append(min(value))
        coordinate, value = [], []
    return result


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
print(solution(100, 97, [[1, 1, 100, 97]]))