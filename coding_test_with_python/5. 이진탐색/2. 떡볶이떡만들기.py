import sys
n, m = map(int, (sys.stdin.readline().split()))
a = list(map(int, sys.stdin.readline().split()))
a.sort()
# print(a)
r = 0
i = 0
cut = max(a) - 1
while r <= m:
    for i in range(n):
        if a[i] - cut > 0:
            r = r + a[i] - cut

    cut = cut - 1

print(cut)