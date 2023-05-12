import sys
from collections import deque

input = sys.stdin.readline
A, B, C = map(int, input().split())
result = set()
visited = [[False] * 201 for _ in range(201)]
queue = deque()
queue.append([0, 0, C])

# BFS
while queue:
    a, b, c = queue.popleft()
    if visited[a][b]:
        continue
    visited[a][b] = True
    if a == 0:
        result.add(c)
    # c to a
    if A < a + c:
        queue.append([A, b, a + c - A])
    else:
        queue.append([a + c, b, 0])
    # b to a
    if A < a + b:
        queue.append([A, a + b - A, c])
    else:
        queue.append([a + b, 0, c])
    # a to b
    if B < b + a:
        queue.append([b + a - B, B, c])
    else:
        queue.append([0, a + b, c])
    # c to b
    if B < b + c:
        queue.append([a, B, b + c - B])
    else:
        queue.append([a, b + c, 0])
    # a to c
    if C < c + a:
        queue.append([a + c - C, b, C])
    else:
        queue.append([0, b, a + c])
    # b to c
    if C < c + b:
        queue.append([a, b + c - C, C])
    else:
        queue.append([a, 0, b + c])

result = sorted(list(result))
print(*result)