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
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if maps[nx][ny] == "X":
                    continue
                count = count + int(maps[nx][ny])
                maps[nx][ny] = "X"
                queue.append([nx, ny])
        return count

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    n, m, result = len(maps), len(maps[0]), []
    for index, value in enumerate(maps):
        maps[index] = list(value)

    for i in range(n):
        for j in range(m):
            if maps[i][j] != "X":
                result.append(bfs(i, j))

    result.sort()
    if result:
        return result
    return [-1]


print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]))
print(solution(["XXX", "XXX", "XXX"]))
