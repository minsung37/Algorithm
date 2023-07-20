import math


def space():
    c = b - a
    n = math.sqrt(c)
    n = math.floor(n)
    if c <= 3:
        print(str(c))
    else:
        x = n ** 2
        y = (n + 1) ** 2
        if c - x > y - c:
            print(2 * n + 1)
        elif c - x == 0:
            print(2 * n - 1)
        else:
            print(2 * n)


# 문제조건 입력받기
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    space()