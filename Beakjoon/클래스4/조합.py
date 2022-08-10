# nCm
n, m = map(int, input().split())
a, b = 1, 1

# 조합의 분자
for i in range(m):
    a = a * n
    n = n - 1
# 조합의 분모
for i in range(m):
    b = b * m
    m = m - 1

# 정답출력
print(a // b)