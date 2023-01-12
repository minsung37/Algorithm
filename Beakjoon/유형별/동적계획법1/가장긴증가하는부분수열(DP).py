# 수열 입력받기
n = int(input())
array = list(map(int, input().split()))

# dp 초기화
dp = [1] * n

# 수열이 97 98 1 99 2 100 3 4 5 101 102 일때
# i가 100이면  99와 2중 긴것을 선택함
# i가 101이면 100과 5중 긴것을 선택함
for i in range(n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# 정답출력
print(max(dp))