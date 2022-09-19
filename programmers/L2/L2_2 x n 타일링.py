# 2 x n 타일링
# https://school.programmers.co.kr/learn/courses/30/lessons/12900
def solution(n):
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
    return dp[-1]


print(solution(4))