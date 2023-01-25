from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    union[x][y] = True
    moves = [[x, y]]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 안에 있고
            if 0 <= nx < n and 0 <= ny < n:
                # 조건에 맞고 연합을 안한 경우
                if l <= abs(graph[x][y] - graph[nx][ny]) <= r and not union[nx][ny]:
                    queue.append([nx, ny])
                    union[nx][ny] = True
                    moves.append([nx, ny])
    return moves


n, l, r = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

union = [[False] * n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

count = 0
while True:
    moves_list = []
    for i in range(n):
        for j in range(n):
            if not union[i][j]:
                temp = bfs(i, j)
                if len(temp) > 1:
                    moves_list.append(temp)
    if len(moves_list) == 0:
        break
    for moves in moves_list:
        p_sum = 0
        for x, y in moves:
            p_sum = p_sum + graph[x][y]
        for x, y in moves:
            graph[x][y] = p_sum // len(moves)
    union = [[False] * n for _ in range(n)]
    count = count + 1


print(count)