import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)
dp[1] = 1

for i in range(2, n + 1):
    value = 5
    j = 1
    while i - j ** 2 >= 0:
        value = min(value, dp[i - j ** 2])
        j = j + 1
    dp[i] = value + 1

print(dp[-1])