import math
# 수 입력 받아서 정렬하기
n = int(input())
array = []
for i in range(n):
    a = int(input())
    array.append(a)
array.sort()

# 인접한 값끼리 빼서 넣기
temp = []
for i in range(1, n):
    b = array[i] - array[i - 1]
    temp.append(b)

# 최대 공약수 구하기
gcd = temp[0]
for i in range(1, n - 1):
    gcd = math.gcd(gcd, temp[i])

# 최대공약수의 약수구하기
result = []
for i in range(1, int(pow(gcd, 1 / 2)) + 1):
    if gcd % i == 0:
        if i ** 2 == gcd:
            result.append(i)
        else:
            result += [i, gcd // i]
result.remove(1)
result.sort()

# 정답출력
for i in range(len(result)):
    print(result[i], end=" ")