# 수 입력받기
n = int(input())

i = 2
while n != 1:
    # n이 i로 나누어 떨어지는경우
    if n % i == 0:
        n = n // i
        print(i)
    # i로 나누어 떨어지지 않는 경우
    else:
        i = i + 1
