import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

# 공기청정기 위치 구하기
cleaner = []
for i in range(r):
    if graph[i][0] == -1:
        cleaner.append([i, 0])
for _ in range(t):
    # 미세먼지 확산
    diffusion = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if graph[x][y] > 0:
                count = 0
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < r and 0 <= ny < c:     # 칸안에 있고
                        if graph[nx][ny] != -1:         # 공기청정기가 아닌경우
                            count = count + 1
                            diffusion[nx][ny] = diffusion[nx][ny] + graph[x][y] // 5
                diffusion[x][y] = diffusion[x][y] - (graph[x][y] // 5) * count
    for i in range(r):
        for j in range(c):
            graph[i][j] = graph[i][j] + diffusion[i][j]

    # 공기 청정기 회전
    up_flow = []
    x, y = cleaner[0][0], cleaner[0][1]
    for i in range(c):
        up_flow.append([x, y + i])
    y = c - 1
    for i in range(1, cleaner[0][0] + 1):
        up_flow.append([x - i, y])
    x = 0
    for i in range(1, c):
        up_flow.append([x, y - i])
    y = 0
    for i in range(1, cleaner[0][0] + 1):
        up_flow.append([x + i, y])

    down_flow = []
    x, y = cleaner[1][0], cleaner[1][1]
    for i in range(c):
        down_flow.append([x, y + i])
    y = c - 1
    for i in range(1, r - cleaner[1][0]):
        down_flow.append([x + i, y])
    x = r - 1
    for i in range(1, c):
        down_flow.append([x, y - i])
    y = 0
    for i in range(1, r - cleaner[1][0]):
        down_flow.append([x - i, y])

    new_up_flow = up_flow[1:]
    up_flow.pop()
    new_down_flow = down_flow[1:]
    down_flow.pop()

    up_temp, down_temp = [], []
    for i in up_flow:
        up_temp.append(graph[i[0]][i[1]])
    for idx, before in enumerate(new_up_flow):
        graph[before[0]][before[1]] = up_temp[idx]

    for i in down_flow:
        down_temp.append(graph[i[0]][i[1]])
    for idx, before in enumerate(new_down_flow):
        graph[before[0]][before[1]] = down_temp[idx]

    for i in cleaner:
        graph[i[0]][i[1]] = -1
        graph[i[0]][i[1] + 1] = 0

result = 2
for i in graph:
    result = result + sum(i)
print(result)