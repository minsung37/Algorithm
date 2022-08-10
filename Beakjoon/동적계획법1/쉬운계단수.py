# 자리수 입력받기
n = int(input())
# dp 테이블 생성
dp = [[0 for i in range(10)] for j in range(n)]
# 초기값 설정
dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# dp 테이블 채우기
for i in range(1, n):
    for j in range(10):
        if j == 0:
            dp[i][0] = dp[i - 1][1]
        elif j == 9:
            dp[i][9] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
# 정답출력
print(sum(dp[n - 1]) % 1000000000)