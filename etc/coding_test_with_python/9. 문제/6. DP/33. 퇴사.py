import sys
input = sys.stdin.readline

# 문제조건 입력받기
n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]

# DP => dp[i] i번째 날부터 마지막 날까지 낼 수 있는 최대 이익
max_value = 0
dp = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    day = schedule[i][0] + i
    # 상담이 기간 안에 끝나는 경우
    if day <= n:
        dp[i] = max(schedule[i][1] + dp[day], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value
# 정답 출력
print(max_value)