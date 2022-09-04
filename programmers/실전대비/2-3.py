from collections import defaultdict
from collections import deque


def solution(n, roads, sources, destination):
    maps = defaultdict(dict)
    result = []
    visited = [-1] * (n + 1)
    visited[destination] = 0

    for road in roads:
        maps[road[0]][road[1]] = 1
        maps[road[1]][road[0]] = 1

    queue = deque()
    queue.append((destination, 0))
    while queue:
        now, count = queue.popleft()
        for i in maps[now]:
            if visited[i] < 0:
                visited[i] = count + 1
                queue.append((i, count + 1))
    for i in sources:
        result.append(visited[i])
    return result


print(solution(3, [[1, 2], [2, 3]], [2, 3], 1))
print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))
