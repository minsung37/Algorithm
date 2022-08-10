from collections import deque
import sys
input = sys.stdin.readline

# 나이트 이동방향
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


# 나이트 이동(BFS)
def bfs(x, y):
    global chess
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if chess[nx][ny] == 0:
                queue.append((nx, ny))
                chess[nx][ny] = chess[x][y] + 1


t = int(input())
for _ in range(t):
    n = int(input())
    chess = [[0] * n for _ in range(n)]
    # 현재좌표
    x, y = map(int, input().split())
    # 타겟좌표
    tx, ty = map(int, input().split())
    # 나이트이동
    bfs(x, y)
    # 현재좌표와 타겟좌표가 같은경우
    if x == tx and y == ty:
        print(0)
    else:
        print(chess[tx][ty])
