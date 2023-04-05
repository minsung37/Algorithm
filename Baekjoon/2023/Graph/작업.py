import sys
input = sys.stdin.readline


n = int(input())
dp = [0] * (n + 1)
for i in range(1, n + 1):
    work, time, *pre_work = map(int, input().split())
    dp[i] = work
    for j in pre_work:
        dp[i] = max(dp[i], dp[j] + work)
print(max(dp))