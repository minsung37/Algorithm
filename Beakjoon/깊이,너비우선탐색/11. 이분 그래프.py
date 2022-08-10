import sys

sys.setrecursionlimit(10 ** 6)


def check(v, graph):  # 정점개수 / 간선개수 / 리스트
    result = [0] * (v + 1)

    def dfs(n, result):
        for i in graph[n]:
            if result[i] == 0:
                result[i] = result[n] % 2 + 1
                dfs(i, result)
            else:
                if result[i] == result[n]:
                    return 1

    # a = True
    for i in range(1, v + 1):
        a = dfs(i, result)
        if a == 1:
            return False
    return True


k = int(sys.stdin.readline())

for _ in range(k):
    v, e = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(v + 1)]
    # print(b)
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    if check(v, graph):
        print('YES')
    else:
        print('NO')