def find(x):
    global parent
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    global parent
    a = find(a)
    b = find(b)
    parent[b] = a


T = int(input())
for t in range(T):
    n = int(input())
    X, Y, tax_rate = list(map(int, input().split())), list(map(int, input().split())), float(input())
    parent, edges = [x for x in range(n)], []
    for i in range(n):
        for j in range(i + 1, n):
            cost = (X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2
            edges.append([cost, i, j])
    edges.sort()
    result, edge_count = 0, n - 1
    for cost, i, j in edges:
        if find(i) != find(j):
            result = result + cost
            union(i, j)
            edge_count = edge_count - 1
            if edge_count == 0:
                break
    print('#{} {}'.format(t + 1, round(result * tax_rate)))