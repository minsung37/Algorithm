# 무인도 여행
# https://school.programmers.co.kr/learn/courses/30/lessons/154540
from collections import deque


def solution(maps):
    def bfs(i, j):
        queue = deque()
        queue.append([i, j])
        count = int(maps[i][j])
        maps[i][j] = "X"
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] != "X":
                        count = count + int(maps[nx][ny])
                        maps[nx][ny] = "X"
                        queue.append([nx, ny])
        return count

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    n, m = len(maps), len(maps[0])
    for i in range(len(maps)):
        maps[i] = list(maps[i])

    result = []
    for i in range(n):
        for j in range(m):
            if maps[i][j] != "X":
                print(i, j)
                result.append(bfs(i, j))
    if not result:
        return [-1]
    result.sort()
    return result


print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]))
print(solution(["XXX", "XXX", "XXX"]))