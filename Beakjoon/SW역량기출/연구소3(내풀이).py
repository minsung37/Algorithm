import copy
from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 바이러스 위치구하기
# -1 벽 -2 비활성 바이러스 0 빈칸 1 바이러스
virus_spot = []
zero = False
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus_spot.append([i, j])
        if graph[i][j] == 1:
            graph[i][j] = -1
        if graph[i][j] == 0:
            zero = True
if not zero:
    print(0)
    exit(0)
virus_comb = list(combinations(virus_spot, m))
init_result = 1000000
result = 1000000
for virus in virus_comb:
    queue = deque()
    copy_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            if copy_graph[i][j] == 2:
                copy_graph[i][j] = 0
    for temp in virus:
        queue.append(temp)
        copy_graph[temp[0]][temp[1]] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if copy_graph[nx][ny] == 0:
                    queue.append([nx, ny])
                    copy_graph[nx][ny] = copy_graph[x][y] + 1
    temp = 0
    in_zero = False
    for x, y in virus_spot:
        copy_graph[x][y] = -2
    for i in range(n):
        for j in range(n):
            if copy_graph[i][j] == 0:
                in_zero = True
            temp = max(temp, copy_graph[i][j])
    if not in_zero:
        result = min(result, temp)
if result == init_result:
    print(-1)
else:
    print(result - 1)