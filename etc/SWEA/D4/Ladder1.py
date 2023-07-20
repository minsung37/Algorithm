# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14ABYKADACFAYh
# 1210. [S/W 문제해결 기본] 2일차 - Ladder1
from collections import deque


for _ in range(10):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(100)]
    # 상 우 좌
    dx = [-1, 0, 0]
    dy = [0, 1, -1]
    queue = deque()
    for idx, x in enumerate(graph[-1]):
        if x == 2:
            queue.append([99, idx])
            break
    while queue:
        x, y = queue.popleft()
        graph[x][y] = 0
        if x == 0:
            print("#{} {}".format(n, y))
            break
        temp = []
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 100 and 0 <= ny < 100:
                if graph[nx][ny] == 1:
                    temp = [nx, ny]
        queue.append(temp)