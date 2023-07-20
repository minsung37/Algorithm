n = int(input())
dp = [1] * (n + 1)
dp[0] = 0
for i in range(2, n + 1):
    dp[i] = dp[i - 2] + dp[i - 1]
print(dp[-1])