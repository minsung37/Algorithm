import sys
# 잔의 갯수 입력받기
n = int(sys.stdin.readline())

# dp테이블 초기화
d = [0] * (n + 1)

# 잔 정보 입력받기
array = [0]
for i in range(n):
    a = int(sys.stdin.readline())
    array.append(a)

# 잔이 1개, 2개 인경우
if n == 1:
    print(sum(array))
elif n == 2:
    print(sum(array))

# 잔이 3개 이상인경우
else:
    d[1] = array[1]
    d[2] = d[1] + array[2]
    d[3] = max(d[1] + array[3], array[2] + array[3], d[2])
    for i in range(4, n + 1):
        d[i] = max(d[i - 2] + array[i], d[i - 3] + array[i - 1] + array[i], d[i - 1])
    print(d[n])
