import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    find = False
    while x <= m * n:
        if (x - y) % n == 0:
            find = True
            break
        x = x + m
    if find:
        print(x)
    else:
        print(-1)