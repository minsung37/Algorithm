# 수 입력받기
n = int(input())
array = list(map(int, input().split()))

# dp
d = [0] * n
d[0] = array[0]

# 이전꺼와 자기자신합 vs 자기자신
for i in range(1, n):
    d[i] = max(array[i], array[i] + d[i - 1])

# 결과출력
print(max(d))