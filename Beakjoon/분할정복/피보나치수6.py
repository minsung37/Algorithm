n = int(input())
x = [[1, 1], [1, 0]]
div = 1000000007


# 행렬곱
def product(x, y):
    res = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] = res[i][j] + x[i][k] * y[k][j]
    for i in range(2):
        for j in range(2):
            res[i][j] = res[i][j] % div
    return res


# 재귀
def recursion(matrix, n):
    if n == 1:
        return matrix
    elif n % 2 == 0:
        matrix = recursion(matrix, n // 2)
        return product(matrix, matrix)
    else:
        matrix = recursion(matrix, n - 1)
        return product(matrix, x)


# 정답출력
k = recursion(x, n)
print(k[1][0] % div)


# 행렬곱으로 피보나치수 찾기
# ㅣF1 F0ㅣ ㅣ1 1ㅣ ^ n  ㅣFn+1  Fn ㅣ
#         *           =
# ㅣF2 F1ㅣ ㅣ1 0ㅣ      ㅣFn+2 Fn+1ㅣ