def solution(arr1, arr2):
    # (a, b) X (b, c)
    a = len(arr1)
    b = len(arr1[0])
    c = len(arr2[0])

    result = [[0] * c for _ in range(a)]
    for i in range(a):
        for j in range(c):
            for k in range(b):
                result[i][j] = result[i][j] + arr1[i][k] * arr2[k][j]

    return result


print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))