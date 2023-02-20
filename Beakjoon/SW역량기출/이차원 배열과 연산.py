import sys
input = sys.stdin.readline


def check_r_and_c():
    global matrix
    row, col = 0, 0
    for i in range(size):
        temp_col = 0
        for j in range(size):
            if matrix[i][j] != 0:
                temp_col = temp_col + 1
            else:
                break
        col = max(col, temp_col)

    for i in range(size):
        temp_row = 0
        for j in range(size):
            if matrix[j][i] != 0:
                temp_row = temp_row + 1
            else:
                break
        row = max(row, temp_row)
    return [row, col]


r, c, k = map(int, input().split())
temp = [list(map(int, input().split())) for _ in range(3)]
size = 100
matrix = [[0] * size for _ in range(size)]
for i in range(len(temp)):
    for j in range(3):
        matrix[i][j] = temp[i][j]

repeat = 0
while True:
    if matrix[r - 1][c - 1] == k:
        break
    if repeat == 100:
        repeat = - 1
        break
    r_and_c = check_r_and_c()
    # R연산
    if r_and_c[0] >= r_and_c[1]:
        for i in range(size):
            curr = matrix[i]
            max_count = max(curr)
            if max_count == 0:
                continue
            counting = [0] * (max_count + 1)
            for j in curr:
                if j != 0:
                    counting[j] = counting[j] + 1
            temp = []
            for index, value in enumerate(counting):
                if index == 0 or value == 0:
                    continue
                temp.append([index, value])
            temp.sort(key=lambda x: (x[1], x[0]))
            new_temp = []
            for x, y in temp:
                new_temp.append(x)
                new_temp.append(y)
            matrix[i] = [0] * size
            for index, value in enumerate(new_temp):
                if index > 100:
                    break
                matrix[i][index] = value
    # C연산
    else:
        for i in range(size):
            curr = []
            for j in range(size):
                curr.append(matrix[j][i])
            max_count = max(curr)
            if max_count == 0:
                continue
            counting = [0] * (max_count + 1)
            for j in curr:
                if j != 0:
                    counting[j] = counting[j] + 1
            temp = []
            for index, value in enumerate(counting):
                if index == 0 or value == 0:
                    continue
                temp.append([index, value])
            temp.sort(key=lambda x: (x[1], x[0]))
            new_temp = []
            for x, y in temp:
                new_temp.append(x)
                new_temp.append(y)
            for j in range(size):
                matrix[j][i] = 0
            for index, value in enumerate(new_temp):
                if index > 100:
                    break
                matrix[index][i] = value
    repeat = repeat + 1
print(repeat)