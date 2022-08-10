import math
# n, k 입력받기
t = int(input())
# 조합
for i in range(t):
    n, m = map(int, input().split())
    mCn = math.factorial(m) / (math.factorial(n) * math.factorial(m - n))
    print(int(mCn))