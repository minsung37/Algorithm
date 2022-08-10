# m ~ n 까지 소수 찾기
m = int(input())
n = int(input())

# 소수의 합을 담을 변수
res = 0
mn = n

# 60 ~ 100 소수 찾기
for i in range(m, n + 1):
    count = 0
    for j in range(1, i + 1):
        # 1부터 n까지 나눈 나머지가 0인경우 count
        if i % j == 0:
            count = count + 1
    # 1부터 n까지 나눈 나머지가 0인경우가 2개 => 소수
    if count == 2:
        res = res + i
        # 소수중 최소값
        if i < mn:
            mn = i

# 소수가 없는 경우
if res == 0:
    print(-1)
# 소수의 합과 그중 최소값을 출력
else:
    print(res)
    print(mn)