# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14geLqABQCFAYD
# 1219. [S/W 문제해결 기본] 4일차 - 길찾기
from collections import defaultdict
from collections import deque


for i in range(10):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    graph = defaultdict(list)
    for j in range(0, 2 * m, 2):
        graph[array[j]].append(array[j + 1])
    queue = deque()
    queue.append(0)
    check = False
    visited = [False] * 100
    visited[0] = True
    while queue:
        x = queue.popleft()
        if x == 99:
            check = True
        for j in graph[x]:
            if not visited[j]:
                queue.append(j)
                visited[j] = True
    print('#{} {}'.format(i + 1, int(check)))