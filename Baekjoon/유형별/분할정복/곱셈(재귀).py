import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())


# (a ** n) % c
def sol(a, n):
    if n == 1:
        return a % c
    else:
        # 짝수인 경우
        if n % 2 == 0:
            return (sol(a, n // 2) ** 2) % c
        # 홀수인 경우
        else:
            return ((sol(a, n // 2) ** 2) * a) % c


# 결과 출력
print(sol(a, b))