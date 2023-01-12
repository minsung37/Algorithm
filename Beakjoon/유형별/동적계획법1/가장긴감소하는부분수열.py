import sys
input = sys.stdin.readline

n = int(input())
temp = list(map(int, input().split()))
array = []
for i in temp:
    array.append(-i)
# DP
dp = [1] * n
for i in range(n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))