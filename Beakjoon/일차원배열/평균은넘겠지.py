import sys
n = int(input())

for i in range(n):
    num = 0
    a = list(map(int, sys.stdin.readline().split()))
    for j in range(a[0]):
        avg = (sum(a) - a[0]) / a[0]
        if a[j + 1] > avg:
            num = num + 1
        rate = num * 100 / a[0]

    print(f'{rate:.3f}%')