import math
import sys
input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    parent[max(a, b)] = min(a, b)


n = int(input())
parent = [x for x in range(n + 1)]
stars = [list(map(float, input().split())) for _ in range(n)]


edges = []
for i in range(0, n - 1):
    for j in range(i + 1, n):
        edges.append((math.sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2), i, j))
edges.sort()

result = 0
for edge in edges:
    cost, x, y = edge
    if find(x) != find(y):
        union(x, y)
        result = result + cost
print(round(result, 2))