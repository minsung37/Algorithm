def dfs(d, x, y):
    global result
    if x == n - 1 and y == n - 1:
        result = result + 1
        return
    # 0우 1대각 2하
    # 우로 이동가능
    if d == 0 or d == 1:
        if y + 1 < n:
            if home[x][y + 1] == 0:
                dfs(0, x, y + 1)
    # 하로 이동가능
    if d == 2 or d == 1:
        if x + 1 < n:
            if home[x + 1][y] == 0:
                dfs(2, x + 1, y)
    # 대각 이동가능
    if x + 1 < n and y + 1 < n:
        if home[x + 1][y] == 0 and home[x][y + 1] == 0 and home[x + 1][y + 1] == 0:
            dfs(1, x + 1, y + 1)


n = int(input())
home = [list(map(int, input().split())) for _ in range(n)]
result = 0
dfs(0, 0, 1)
print(result)