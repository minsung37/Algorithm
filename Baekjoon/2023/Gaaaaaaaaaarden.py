from collections import deque


def select_red_and_green(depth, index):
    if depth == g + r:
        visited = [False] * (g + r)
        separate_red_and_green(0, 0, visited)
        return
    for i in range(index, len(water)):
        candidate.append(water[i])
        select_red_and_green(depth + 1, i + 1)
        candidate.pop()


def separate_red_and_green(depth, index, visited):
    global result
    if depth == g:
        result = max(result, get_flower_count(visited))
        return
    for i in range(index, g + r):
        visited[i] = True
        separate_red_and_green(depth + 1, i + 1, visited)
        visited[i] = False


def get_flower_count(visited):
    red_list = []
    green_list = []
    for i in range(g + r):
        if not visited[i]:
            red_list.append([candidate[i] // mod, candidate[i] % mod])
    for i in range(g + r):
        if visited[i]:
            green_list.append([candidate[i] // mod, candidate[i] % mod])
    return bfs(red_list, green_list)


def bfs(red_list, green_list):
    # 1 red 2 green 3 flower
    flower = 0
    spread = [[[0, 0] for _ in range(m)] for _ in range(n)]
    queue = deque()
    for x, y in red_list:
        spread[x][y][1] = 1
        queue.append([x, y])
    for x, y in green_list:
        spread[x][y][1] = 2
        queue.append([x, y])

    while queue:
        x, y = queue.popleft()
        # 꽃핀경우
        if spread[x][y][1] == 3:
            continue
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 범위 벗어난 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 물인경우
            if ground_origin[nx][ny] == 0:
                continue
            # 배양액 뿌리기
            if spread[nx][ny][1] == 0:
                spread[nx][ny][0] = spread[x][y][0] + 1
                spread[nx][ny][1] = spread[x][y][1]
                queue.append([nx, ny])
            # 꽃이 피는 경우
            elif spread[nx][ny][1] == 1:
                if spread[x][y][1] == 2 and spread[x][y][0] + 1 == spread[nx][ny][0]:
                    spread[nx][ny][1] = 3
                    flower = flower + 1
            elif spread[nx][ny][1] == 2:
                if spread[x][y][1] == 1 and spread[x][y][0] + 1 == spread[nx][ny][0]:
                    spread[nx][ny][1] = 3
                    flower = flower + 1
    return flower


n, m, g, r = map(int, input().split())
ground_origin = [list(map(int, input().split())) for _ in range(n)]
mod, water, candidate = 500, [], []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for i in range(n):
    for j in range(m):
        if ground_origin[i][j] == 2:
            water.append(i * mod + j)
result = 0
select_red_and_green(0, 0)
print(result)