from collections import deque
import copy
import sys
input = sys.stdin.readline

# 그래프 입력받기
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 방향
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 안전영역
safety = 0


# 벽만들기
def makeWall(count):
    # 벽 3개 설치하면 탐색시작
    if count == 3:
        bfs()
        return
    # 벽설치
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(count + 1)
                graph[i][j] = 0


# 바이러스 퍼지기, 안전영역 카운트
def bfs():
    global safety
    queue = deque()
    # 그래프 복사
    temp_graph = copy.deepcopy(graph)
    # 바이러스 좌표 큐에 넣기
    for i in range(n):
        for j in range(m):
            if temp_graph[i][j] == 2:
                queue.append((i, j))
    # 바이러스 퍼지기
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 빈칸인 경우
            if temp_graph[nx][ny] == 0:
                temp_graph[nx][ny] = 2
                queue.append((nx, ny))
    # 안전 영역 카운트
    count = 0
    for i in range(n):
        count = count + temp_graph[i].count(0)
    safety = max(safety, count)


# 체크
makeWall(0)
print(safety)