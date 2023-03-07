import math
# m이상 n이하 소수 출력
m, n = map(int, (input().split()))


# 소수판별 2부터 루트값+1 까지만 확인하면 됨
def is_prime_number(x):
    if x == 1:
        return
    for j in range(2, int(math.sqrt(x)) + 1):
        if x % j == 0:
            return
    return x


for i in range(m, n + 1):
    res = is_prime_number(i)
    # 값이 존재하면 => 소수이면 출력
    if res is not None:
        print(res)