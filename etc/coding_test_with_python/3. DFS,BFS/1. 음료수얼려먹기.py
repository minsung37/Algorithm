n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x,y):
    # x > n이 아닌이유는 상하좌우 dfs호출시 범위 벗어남!!
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False


res = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            res = res + 1


print(res)