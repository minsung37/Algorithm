from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline


def is_seven(comb):
    s_count, y_count = 0, 0
    for x, y in comb:
        if graph[x][y] == 'S':
            s_count = s_count + 1
        else:
            y_count = y_count + 1
    if s_count >= 4:
        return True
    return False


def is_near(comb):
    visited = [False] * 7
    queue = deque()
    queue.append(comb[0])
    visited[0] = True
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if (nx, ny) in comb:
                next = comb.index((nx, ny))
                if not visited[next]:
                    queue.append((nx, ny))
                    visited[next] = True
    if False in visited:
        return False
    return True


size = 5
graph = [list(input()) for _ in range(size)]
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
result = 0
coordinate_list = [(x, y) for x in range(size) for y in range(size)]
coordinates = list(combinations(coordinate_list, 7))
for coordinate in coordinates:
    if not is_seven(coordinate):
        continue
    if is_near(coordinate):
        result = result + 1
print(result)