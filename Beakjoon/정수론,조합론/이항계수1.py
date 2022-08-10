import math
# n, k 입력받기
n, k = map(int, input().split())

nCk = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
print(int(nCk))