import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))
dp = [0] * (n + 1)

result = 0
for i in range(n):
    result = result + array[i]
    dp[i + 1] = result

for _ in range(m):
    a, b = map(int, input().split())
    print(dp[b] - dp[a - 1])