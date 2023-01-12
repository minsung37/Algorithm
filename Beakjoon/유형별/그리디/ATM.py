n = int(input())
a = list(map(int, input().split()))
a.sort()
time = 0
t = []
for i in range(n):
    time = time + a[i]
    t.append(time)
print(sum(t))