import sys
input = sys.stdin.readline


def dfs(x, y, count):
    global result, visited
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue
        if visited[ord(ground[nx][ny]) - ord("A")]:
            result = max(result, count)
        else:
            visited[ord(ground[nx][ny]) - ord("A")] = True
            dfs(nx, ny, count + 1)
            visited[ord(ground[nx][ny]) - ord("A")] = False


r, c = map(int, input().split())
ground = [list(input()) for _ in range(r)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

result = 0
visited = [False] * 26
visited[ord(ground[0][0]) - ord("A")] = True
dfs(0, 0, 1)
print(result)