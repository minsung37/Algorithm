# https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 게임 맵 최단거리
from collections import deque


def solution(maps):
    n, m = len(maps[0]), len(maps)
    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

    queue = deque()
    queue.append((0, 0))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if maps[nx][ny] == 1:
                queue.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1
    if maps[-1][-1] == 1:
        return -1
    return maps[-1][-1]


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1], [1, 0, 1, 1, 1],
                [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
