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


# 문제입력 받기
n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append([cost, a, b])
edges.sort()

# 최소비용 길 만들기
parent = [x for x in range(n + 1)]
result, last_edge_cost, count = 0, 0, 0
for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        result = result + cost
        last_edge_cost = cost

# 가장 비싼길 제외
print(result - last_edge_cost)