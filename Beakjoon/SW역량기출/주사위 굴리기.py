import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())

# 동 서 북 남
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
direction = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0]

for d in direction:
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < n and 0 <= ny < m:
        if d == 1:
            dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
        elif d == 2:
            dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
        elif d == 3:
            dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
        else:
            dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
        print(dice[0])
        x, y = nx, ny
        if graph[x][y] == 0:
            graph[x][y] = dice[5]
        else:
            dice[5] = graph[x][y]
            graph[x][y] = 0
