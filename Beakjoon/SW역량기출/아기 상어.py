from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
start_x, start_y = 0, 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            start_x, start_y = i, j
            graph[i][j] = 0
size, eat, result = 2, 0, 0

queue = deque()
while True:
    # 방문 가능한곳의 거리 구하기
    queue.append([start_x, start_y])
    visited = [[-1] * n for _ in range(n)]
    visited[start_x][start_y] = 0
    feed_list = []
    while queue:
        x, y = queue.popleft()
        # 먹이후보
        if 0 < graph[x][y] < size:
            feed_list.append([visited[x][y], x, y])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:  # 좌표안에 있고
                if visited[nx][ny] == -1 and graph[nx][ny] <= size:  # 방문하지 않은경우와 자신보다 작거나 같은 물고기
                    queue.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1
    # 가깝고, 가장위, 가장왼쪽
    feed_list.sort(key=lambda x: (x[0], x[1], x[2]))

    # 먹이 있는 경우
    if feed_list:
        distance, x, y = feed_list[0]
        result = result + distance
        graph[x][y] = 0
        start_x, start_y = x, y
        eat = eat + 1
        if size == eat:
            size = size + 1
            eat = 0
    else:
        break
print(result)
