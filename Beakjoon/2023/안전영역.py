import copy
from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y):
    global city
    queue = deque()
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if city[nx][ny] != 0:
                    city[nx][ny] = 0
                    queue.append([nx, ny])


n = int(input())
city_original = [list(map(int, input().split())) for _ in range(n)]
min_rain = 101
max_rain = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in city_original:
    max_rain = max(max_rain, max(i))
    min_rain = min(min_rain, min(i))

result = 1
for rain in range(min_rain, max_rain):
    city = copy.deepcopy(city_original)
    for i in range(n):
        for j in range(n):
            if city[i][j] <= rain:
                city[i][j] = 0
    # 안전구역 찾기
    count = 0
    for i in range(n):
        for j in range(n):
            if city[i][j] != 0:
                bfs(i, j)
                count = count + 1
    result = max(result, count)
print(result)