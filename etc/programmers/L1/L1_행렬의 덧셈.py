# 행렬의 덧셈
# https://school.programmers.co.kr/learn/courses/30/lessons/12950
def solution(arr1, arr2):
    n, m = len(arr1), len(arr1[0])
    result = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            result[i][j] = arr1[i][j] + arr2[i][j]

    return result


print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
print(solution([[1], [2]], [[3], [4]]))
