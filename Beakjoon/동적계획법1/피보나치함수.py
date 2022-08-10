# 반복횟수 입력받기
n = int(input())

# 입력받은값 리스트에 담기
array = []
for i in range(n):
    array.append(int(input()))

# n이 40까지 이므로
array0 = [0] * 41
array1 = [0] * 41

# 초기값
array0[0] = 1
array1[1] = 1

# 점화식
for i in array:
    for j in range(2, i + 1):
        array0[j] = array0[j - 1] + array0[j - 2]
        array1[j] = array1[j - 1] + array1[j - 2]

# 정답 출력
for i in array:
    print(array0[i], end=" ")
    print(array1[i])
