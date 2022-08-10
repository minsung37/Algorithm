import sys
# 문자 입력받기
a = sys.stdin.readline().strip().upper()
b = sys.stdin.readline().strip().upper()
n = len(a)
m = len(b)

# dp 테이블 만들기
dp = [[0] * (m + 1) for _ in range(n + 1)]

# dp
for i in range(1, n + 1):
    for j in range(1, m + 1):
        # 끝에 추가된 문자를 비교
        # 같은경우
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        # 다른경우
        # 인접한 경우에서 가장 문자열 고르기
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])