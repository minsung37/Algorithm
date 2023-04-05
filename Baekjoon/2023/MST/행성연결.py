import sys
input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    parent[max(x, y)] = min(x, y)


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
parent = [x for x in range(n)]
# 비용순으로 정렬
edges = []
for i in range(n):
    for j in range(n):
        if i != j:
            edges.append([graph[i][j], i, j])
edges.sort()
# 최소비용 구하기
result = 0
for cost, x, y in edges:
    if find(x) != find(y):
        union(x, y)
        result = result + graph[x][y]
print(result)