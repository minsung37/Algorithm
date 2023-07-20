# 개수, 제한무게 입력받기
n, k = map(int, input().split())

# 무게 가치 입력받기
array = [[0, 0]]
for i in range(n):
    b = list(map(int, input().split()))
    array.append(b)

# dp테이블 만들기
dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight = array[i][0]
        values = array[i][1]
        if j < weight:
            # 가방에 안들어가면 이전에 가능한 경우 가져옴
            dp[i][j] = dp[i - 1][j]
        else:
            # 가방에 들어가는 경우 이전 경우와
            # 현재무게에 알맞는 최소 조합을 가져와서 현재 가치 더하기
            # ex 무게 3인 경우 3의 가치인 6과 (7 - 3) 의 무게를 가지는 가방의 가치를 더함
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + values)

# 정답출력
print(dp[n][k])
# 4 7
# 6 13
# 4 8
# 3 6
# 5 12