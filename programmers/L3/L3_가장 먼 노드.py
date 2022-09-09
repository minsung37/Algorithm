# https://school.programmers.co.kr/learn/courses/30/lessons/49189
# 가장 먼 노드
from collections import deque


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)

    visited = [0] * (n + 1)
    visited[1] = 1
    queue = deque([1])

    while queue:
        n = queue.popleft()
        for i in graph[n]:
            # 첫 방문인 경우
            if visited[i] == 0:
                visited[i] = visited[n] + 1
                queue.append(i)

    return visited.count(max(visited))


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))