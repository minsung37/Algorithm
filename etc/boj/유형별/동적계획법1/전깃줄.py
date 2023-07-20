# 줄의 개수와 연결정보 입력받기
n = int(input())
array = []
for i in range(n):
    temp = list(map(int, input().split()))
    array.append(temp)

# 첫번째 줄을 기준으로 정렬하기
array.sort()

# dp
# 두번째 줄을 기준으로 가장긴 증가하는 부분수열
dp = [1] * n
for i in range(n):
    for j in range(i):
        if array[i][1] > array[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

# 정답출력
print(n - max(dp))