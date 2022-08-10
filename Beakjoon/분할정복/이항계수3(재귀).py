# 문제 정보 입력받기
n, k = map(int, input().split())
P = 1000000007


# 펙토리얼 구하기
def factorial(a, mod):
    res = 1
    for i in range(2, a + 1):
        res = (res * i) % mod
    return res


# (a ** p) % mod 구하기
def sol(a, p, mod):
    if p == 1:
        return a % mod
    if p % 2 == 1:
        return ((sol(a, p // 2, mod) ** 2) * a) % mod
    else:
        return ((sol(a, p // 2, mod) ** 2) * 1) % mod


# 페르마의 소정리 이용
# x = (k! * (n - k)!) % P
# nRk & P => (n! % P) * ((x) ** (P - 2)) % P
result = (factorial(n, P) * sol(factorial(k, P) * factorial(n - k, P), P - 2, P)) % P
print(result)