# https://school.programmers.co.kr/learn/courses/30/lessons/49191
# 순위
import copy
from collections import deque


def solution(n, results):
    win, lose = [[] for _ in range(n + 1)], [[] for _ in range(n + 1)]
    for x, y in results:
        win[x].append(y)
        lose[y].append(x)

    visited_init = [False] * (n + 1)
    count = 0
    for i in range(1, n + 1):
        visited = copy.deepcopy(visited_init)
        visited[0] = True
        visited[i] = True
        for n in [win, lose]:
            queue = deque([i])
            while queue:
                v = queue.popleft()
                for node in n[v]:
                    if not visited[node]:
                        visited[node] = True
                        queue.append(node)
        if False not in visited:
            count = count + 1
    return count


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))