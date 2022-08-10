import sys
input = sys.stdin.readline

n = int(input())
cost = list(map(int, input().split()))

# DP
dp = [0] + cost
for i in range(1, n + 1):
    for j in range(i):
        dp[i] = max(dp[i], dp[i - j] + dp[j])
print(dp[-1])