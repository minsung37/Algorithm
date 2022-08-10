# 문제조건 입력받기
n = int(input())
a = list(map(int, input().split()))

# 소수의 개수를 담을 변수
res = 0

# 소수판별
for i in a:
    count = 0
    for j in range(1, i + 1):
        # 1부터 n까지 나눈 나머지가 0인경우 count
        if i % j == 0:
            count = count + 1
    # 1부터 n까지 나눈 나머지가 0인경우가 2개 => 소수
    if count == 2:
        res = res + 1

# 정답출력
print(res)