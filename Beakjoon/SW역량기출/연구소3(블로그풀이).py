from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline


def bfs(queue, blank):
    visited = [[False] * n for _ in range(n)]
    time = 0
    while True:
        new_virus_count = len(queue)
        # 종료조건
        if blank == 0:
            return time
        if new_virus_count == 0 and blank > 0:
            return INF
        time = time + 1
        for _ in range(new_virus_count):
            x, y = queue.popleft()
            visited[x][y] = True
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    if not visited[nx][ny]:
                        # 벽만난경우
                        if graph[nx][ny] == 0:
                            queue.append([nx, ny])
                            visited[nx][ny] = True
                            blank = blank - 1
                        # 바이러스 만난경우
                        elif graph[nx][ny] == 2:
                            queue.append([nx, ny])
                            visited[nx][ny] = True


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 바이러스 위치구하기
virus_spot = []
blank = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus_spot.append([i, j])
        if graph[i][j] == 0:
            blank = blank + 1

virus_comb = list(combinations(virus_spot, m))
INF = 100000
result = INF

for virus_list in virus_comb:
    queue = deque()
    for virus in virus_list:
        queue.append(virus)
    tmp = bfs(queue, blank)
    result = min(result, tmp)
if result == INF:
    print(-1)
else:
    print(result)