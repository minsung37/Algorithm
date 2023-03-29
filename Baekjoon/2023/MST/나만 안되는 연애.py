import sys
input = sys.stdin.readline


def find(x):
    global parent
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    global parent
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
info = [" "] + list(input().split())
parent = [x for x in range(n + 1)]
edges = []
for _ in range(m):
    u, v, d = map(int, input().split())
    edges.append([d, u, v])
edges.sort()
result = 0
edge_count = n - 1
for cost, u, v in edges:
    if info[u] == info[v]:
        continue
    if find(u) != find(v):
        result = result + cost
        union(u, v)
        edge_count = edge_count - 1
        if edge_count == 0:
            break
if edge_count != 0:
    result = -1
print(result)