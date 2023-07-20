# 땅따먹기
# https://school.programmers.co.kr/learn/courses/30/lessons/12913
import copy


def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            k = max(land[i - 1])
            k_index = land[i - 1].index(k)
            if j == k_index:
                temp = copy.copy(land[i - 1])
                temp.remove(k)
                land[i][j] = land[i][j] + max(temp)
            else:
                land[i][j] = land[i][j] + k
    return max(land[-1])


def solution_better(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] = max(land[i - 1][: j] + land[i - 1][j + 1:]) + land[i][j]
    return max(land[-1])


print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
