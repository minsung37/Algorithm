# 3 x n 타일링
# https://school.programmers.co.kr/learn/courses/30/lessons/12902
def solution(n):
    dp = [1] * 2501
    for i in range(1, 2501):
        dp[i] = dp[i - 1] * 3
        dp[i] = (dp[i] + 2 * sum(dp[:i - 1])) % 1000000007
    if n % 2 == 1:
        return 0
    else:
        return dp[n // 2]


print(solution(4))
print(solution(6))
print(solution(8))