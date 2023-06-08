from collections import deque
import sys
input = sys.stdin.readline

# n x n칸, 바이러스 번호 k
n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# s초후 (x, y)칸의 바이러스 종류
s, x, y = map(int, input().split())

# 방향
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 바이러스 위치 리스트에 저장 => 순서대로 큐에 넣기
virus = []
for i in range(n):
    for j in range(n):
        num = graph[i][j]
        # 바이러스 있는 경우
        if num != 0:
            virus.append((num, 0, i, j))
virus.sort()
queue = deque(virus)


# 바이러스 퍼짐
while queue:
    # 바이러스번호, 시간, 좌표
    a, time, b, c = queue.popleft()
    # 시간 되면
    if time == s:
        break
    for i in range(4):
        nx = b + dx[i]
        ny = c + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = a
                queue.append((a, time + 1, nx, ny))

# 정답출력
print(graph[x - 1][y - 1])
