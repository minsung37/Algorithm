import sys
input = sys.stdin.readline

n = int(input())
graph = [[0] * 101 for _ in range(101)]

# 하 좌 상 우
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(n):
    x, y, d, g = map(int, input().split())
    direction = [d]
    graph[x][y] = 1
    for i in range(g):
        temp = []
        for d in reversed(direction):
            temp.append((d + 1) % 4)
        direction = direction + temp
    for d in direction:
        x = x + dx[d]
        y = y + dy[d]
        graph[x][y] = 1

result = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1 and graph[i + 1][j] == 1 and graph[i][j + 1] == 1 and graph[i + 1][j + 1] == 1:
            result = result + 1

print(result)