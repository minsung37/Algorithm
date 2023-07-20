import sys
input = sys.stdin.readline


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    parent[max(a, b)] = min(a, b)


n, m = map(int, input().split())
parent = [x for x in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    if find(a) != find(b):
        union(a, b)
    # 사이클이 형성된경우
    else:
        print(i + 1)
        exit(0)
print(0)