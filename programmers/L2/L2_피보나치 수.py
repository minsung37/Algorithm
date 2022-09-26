# 피보나치 수
# https://school.programmers.co.kr/learn/courses/30/lessons/12945
def solution(n):
    dp = [0] * n
    dp[0], dp[1] = 1, 1
    for i in range(2, n):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567
    return dp[-1]


print(solution(2))
print(solution(3))
print(solution(5))