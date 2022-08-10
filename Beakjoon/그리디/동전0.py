n, k = map(int, input().split())
a = []
coin = 0

for i in range(n):
    m = int(input())
    a.append(m)

a.sort(reverse=True)

for j in range(len(a)):
    if k % a[j] < k:
        coin = coin + k // a[j]
        k = k % a[j]

print(coin)