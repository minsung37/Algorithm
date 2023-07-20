# dp만들기
dp = [0] * 11
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, 11):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

# 입력값 받기
t = int(input())
for i in range(t):
    a = int(input())
    print(dp[a])