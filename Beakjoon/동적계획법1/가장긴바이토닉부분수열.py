# 수열 입력받기
n = int(input())
array = list(map(int, input().split()))

# 감소하는 부분 찾기위해 리스트 뒤집기
array_R = list(reversed(array))

# inc 증가하는 부분, dec 감소하는 부분
inc = [1] * n
dec = [1] * n

# 가장긴 증가하는 부분 수열 알고리즘
for i in range(n):
    for j in range(i):
        if array[i] > array[j]:
            inc[i] = max(inc[i], inc[j] + 1)
        if array_R[i] > array_R[j]:
            dec[i] = max(dec[i], dec[j] + 1)

# 감소하는 부분 뒤집기
dec = list(reversed(dec))
res = []
for i in range(n):
    res.append(dec[i] + inc[i])

# 정답출력
print(max(res) - 1)