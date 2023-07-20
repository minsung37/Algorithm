from collections import deque
import sys
input = sys.stdin.readline

# 방향 설정
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    count = 1
    graph[x][y] = 0
    # 큐가 빌때까지 반복
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 방문한경우
            if graph[nx][ny]:
                count = count + 1
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return count


t = int(input())
for _ in range(t):
    array = []
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        # 주의할곳!!!!
        graph[y][x] = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                array.append(bfs(i, j))
    print(len(array))
