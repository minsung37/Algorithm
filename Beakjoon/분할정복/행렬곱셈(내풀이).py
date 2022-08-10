# A x B 행렬곱 계산
# A 행렬 입력받기
n1, m1 = map(int, input().split())
a = []
for i in range(n1):
    temp = list(map(int, input().split()))
    a.append(temp)

# B 행열 입력받기
n2, m2 = map(int, input().split())
b = []
for i in range(n2):
    temp = list(map(int, input().split()))
    b.append(temp)

# 행렬의 하나의 성분을 구성하는요소들 리스트에 담기
res = []
for k in range(n2):
    array = []
    for i in range(n1):
        for j in range(m2):
            array.append(a[i][k] * b[k][j])
    res.append(array)

# 각각 더해서 최종 행렬값 리스트에 담기
result = []
for i in range(len(res[0])):
    temp = 0
    for j in range(len(res)):
        temp = temp + res[j][i]
    result.append(temp)

k = 0
# 정답 출력
while k < n1*m2:
    if (k + 1) % n1 == 0:
        print(result[k])
    else:
        print(result[k], end=" ")
    k = k + 1
print(result)
print(res)