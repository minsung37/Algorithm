n, m = map(int, input().split())
temp = 0
for i in range(n):
    a = list(map(int, input().split()))
    if temp < min(a):
        temp = min(a)

print(temp)