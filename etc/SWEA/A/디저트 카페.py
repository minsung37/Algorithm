def dfs(x, y, d, disert):
    global ix, iy, result
    if d == 3 and x == ix and y == iy:
        result = max(result, len(disert))
        return
    if d == 3:
        nx = x + dx[3]
        ny = y + dy[3]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] not in disert:
                dfs(nx, ny, 3, [graph[nx][ny]] + disert)
    else:
        for i in range(2):
            nx = x + dx[d + i]
            ny = y + dy[d + i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] not in disert:
                    dfs(nx, ny, d + i, [graph[nx][ny]] + disert)


T = int(input())
for t in range(T):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    dx = [1, -1, -1, 1]
    dy = [1, 1, -1, -1]
    result = -1
    ix, iy = 0, 0
    for i in range(n):
        for j in range(n):
            ix, iy = i, j
            dfs(i, j, 0, [])
    print('#{} {}'.format(t + 1, result))