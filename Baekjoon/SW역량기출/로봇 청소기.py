from collections import deque


n, m = map(int, input().split())
graph = []
queue = deque()
queue.append(list(map(int, input().split())))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for _ in range(n):
    graph.append(list(map(int, input().split())))


count = 0
while queue:
    x, y, d = queue.popleft()
    if graph[x][y] == 0:
        graph[x][y] = 2
        count = count + 1
    temp_d = d
    for i in range(4):
        temp_d = (temp_d + 3) % 4
        nx = x + dx[temp_d]
        ny = y + dy[temp_d]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            queue.append([nx, ny, temp_d])
            break
        elif i == 3:
            nx = x - dx[d]
            ny = y - dy[d]
            if 0 <= nx <= n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    break
                else:
                    queue.append([nx, ny, d])
print(count)