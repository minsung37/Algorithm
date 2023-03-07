n1, m1 = map(int, input().split())
a = []
for _ in range(n1):
    a.append(list(map(int, input().split())))

n2, m2 = map(int, input().split())
b = []
for _ in range(n2):
    b.append(list(map(int, input().split())))

# 행렬 곱셈
res = [[0 for _ in range(m2)] for _ in range(n1)]
for i in range(n1):
    for j in range(m2):
        for k in range(m1):
            res[i][j] = res[i][j] + a[i][k] * b[k][j]

# 정답 출력
for i in res:
    for j in i:
        print(j, end=' ')
    print()