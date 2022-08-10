# 입력값 받기
n = int(input())
# dp 테이블 만들기
dp = [1] * (n + 1)
for i in range(2, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007
# 정답출력
print(dp[n])