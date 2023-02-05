# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14BgD6AEECFAYh
# 1211. [S/W 문제해결 기본] 2일차 - Ladder2
import copy
from collections import deque


def bfs(v):
    queue = deque()
    count = 0
    queue.append(v)
    graph_copy = copy.deepcopy(graph)
    while queue:
        x, y = queue.popleft()
        graph_copy[x][y] = 0
        if x == 99:
            return [v[1], count]
        temp = []
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 100 and 0 <= ny < 100:
                if graph_copy[nx][ny] == 1:
                    temp = [nx, ny]
        if len(temp) > 0:
            count = count + 1
            queue.append(temp)


for _ in range(10):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(100)]
    # 하 우 좌
    dx = [1, 0, 0]
    dy = [0, 1, -1]
    start_list = []
    for idx, y in enumerate(graph[0]):
        if y == 1:
            start_list.append([0, idx])
    result = []
    for start in start_list:
        k = bfs(start)
        if k:
            result.append(k)
    result.sort(key=lambda x: x[1])
    print("#{} {}".format(n, result[0][0]))
