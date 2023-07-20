# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14dUIaAAUCFAYD
# 1217. [S/W 문제해결 기본] 4일차 - 거듭 제곱
def sol(n, m):
    if m == 0:
        return 1
    return n * sol(n, m - 1)


for i in range(10):
    t = input()
    n, m = map(int, input().split())
    print('#{} {}'.format(i + 1, sol(n, m)))