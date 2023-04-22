from collections import deque


def solution(maps):
    def bfs(arrive, end):
        nonlocal answer
        visited = [[False] * m for _ in range(n)]
        queue = deque()
        queue.append(arrive + [0])
        visited[arrive[0]][arrive[1]] = True
        while queue:
            x, y, count = queue.popleft()
            if [x, y] == end:
                answer = answer + count
                return True
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if visited[nx][ny]:
                    continue
                if maps[nx][ny] == "X":
                    continue
                queue.append([nx, ny, count + 1])
                visited[nx][ny] = True
        return False

    n, m = len(maps), len(maps[0])
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    # 시작, 레버, 목표점 좌표
    sx, sy, lx, ly, ex, ey = 0, 0, 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                sx, sy = i, j
            if maps[i][j] == "L":
                lx, ly = i, j
            if maps[i][j] == "E":
                ex, ey = i, j

    answer = 0
    if bfs([sx, sy], [lx, ly]):
        if bfs([lx, ly], [ex, ey]):
            return answer
    return -1


print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]))
print(solution(["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]))