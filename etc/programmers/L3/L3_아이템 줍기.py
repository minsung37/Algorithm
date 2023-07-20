# https://school.programmers.co.kr/learn/courses/30/lessons/87694
# 아이템 줍기
from collections import deque


def solution(rectangle, start_x, start_y, target_x, target_y):
    # 테두리 판단
    def is_border(tx, ty):
        for d in range(8):
            ntx = tx + dtx[d]
            nty = ty + dty[d]
            if graph[ntx][nty] == 0:
                return True
        # 8방 탐색 했을때 모든 점이 사각형 내부 점이라면 모서리가 아니다.
        return False

    # 배율
    zoom = 2
    for index, value in enumerate(rectangle):
        for i in range(4):
            value[i] = value[i] * zoom
        rectangle[index] = value
    start_x = start_x * zoom
    start_y = start_y * zoom
    target_x = target_x * zoom
    target_y = target_y * zoom
    answer = 0

    # 다음점 탐색
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # 모서리 탐색
    dtx = [1, 0, -1, 0, 1, 1, -1, -1]
    dty = [0, 1, 0, -1, -1, 1, 1, -1]

    # 사각형 그리기
    size = 51 * zoom
    graph = [[0] * size for _ in range(size)]
    for lx, ly, rx, ry in rectangle:
        for x in range(lx, rx + 1):
            for y in range(ly, ry + 1):
                graph[x][y] = 1

    # BFS
    queue = deque()
    queue.append([start_x, start_y, 0])
    visited = [[False] * size for _ in range(size)]
    visited[start_x][start_y] = True
    while queue:
        x, y, count = queue.popleft()
        if x == target_x and y == target_y:
            answer = count
            break
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 방문하지 않고 모서리의 후보인경우
            if not visited[nx][ny] and graph[nx][ny] == 1:
                # 모서리인 경우
                if is_border(nx, ny):
                    queue.append([nx, ny, count + 1])
                    visited[nx][ny] = True
    return answer // zoom


print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
print(solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1))
print(solution([[1, 1, 5, 7]], 1, 1, 4, 7))
print(solution([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10))
print(solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3))
print(solution([[1, 1, 3, 7], [2, 2, 7, 4], [4, 3, 6, 6]], 1, 2, 6, 6))
