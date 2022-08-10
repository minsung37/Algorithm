import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if graph[x][y] == 1:
        # 해당 노드 방문처리
        graph[x][y] = 0
        # 상, 하, 좌, 우 재귀적으로 탐색
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False


t = int(input())
for _ in range(t):
    count = 0
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                count = count + 1
    print(count)