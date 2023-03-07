import sys
from collections import defaultdict
from itertools import combinations
from collections import deque
input = sys.stdin.readline


def bfs(v, other):
    queue = deque()
    visited = [False] * (n + 1)
    check = set()
    queue.append(v)
    while queue:
        x = queue.popleft()
        check.add(x)
        visited[x] = True
        # 그래프를 돌면서 방문한적 없고 상대구를 방문하지 않는 경우
        for i in graph[x]:
            if not visited[i] and i not in other:
                queue.append(i)
                visited[i] = True
    return check


# 인구수
n = int(input())
population = list(map(int, input().split()))

# 연결정보
graph = defaultdict(list)
for i in range(n):
    info = list(map(int, input().split()))
    count = info[0]
    for j in range(count):
        graph[i + 1].append(info[j + 1])

# 후보구역
city = [x + 1 for x in range(n)]
gerrymandering = []
for i in range(n // 2):
    gerrymandering = gerrymandering + list(combinations(city, (i + 1)))

# 내구역, 상대구역 탐색
result = []
city = set(city)
for gerry in gerrymandering:
    gerry_set = set(gerry)
    other = list(city - gerry_set)
    check_gerry = bfs(gerry[0], other)
    check_other = bfs(other[0], gerry)
    other = set(other)
    # 상대구역에 가지않고 내구역 모두 방문하는지 체크
    if check_gerry == gerry_set and check_other == other:
        one, two = 0, 0
        for i in check_gerry:
            one = one + population[i - 1]
        for i in check_other:
            two = two + population[i - 1]
        result.append(abs(one - two))

if not result:
    print(-1)
else:
    print(min(result))