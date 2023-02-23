import sys
input = sys.stdin.readline


def check_matrix(trans_matrix):
    for i in trans_matrix:
        if sum(i) % 2 == 1:
            return False
    for i in range(n):
        temp = 0
        for j in range(n):
            temp = temp + trans_matrix[j][i]
        if temp % 2 == 1:
            return False
    return True


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
if check_matrix(matrix):
    print("OK")
    exit(0)
else:
    for i in range(n):
        for j in range(n):
            matrix[i][j] = (matrix[i][j] + 1) % 2
            if check_matrix(matrix):
                print("Change bit ({},{})".format(i + 1, j + 1))
                exit(0)
            matrix[i][j] = (matrix[i][j] + 1) % 2
print("Corrupt")