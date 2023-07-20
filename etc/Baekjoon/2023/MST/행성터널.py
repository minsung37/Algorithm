import heapq
import sys
input = sys.stdin.readline


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
parent = [x for x in range(n)]
x, y, z = [], [], []
for i in range(n):
    a, b, c = map(int, input().split())
    x.append([a, i])
    y.append([b, i])
    z.append([c, i])
x.sort()
y.sort()
z.sort()

heap = []
for i in range(n - 1):
    heapq.heappush(heap, (abs(x[i][0] - x[i + 1][0]), x[i][1], x[i + 1][1]))
    heapq.heappush(heap, (abs(y[i][0] - y[i + 1][0]), y[i][1], y[i + 1][1]))
    heapq.heappush(heap, (abs(z[i][0] - z[i + 1][0]), z[i][1], z[i + 1][1]))

result, count = 0, n - 1
while count != 0:
    cost, i, j = heapq.heappop(heap)
    if find(i) != find(j):
        union(i, j)
        result = result + cost
        count = count - 1
print(result)