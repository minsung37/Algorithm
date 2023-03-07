from collections import deque
import sys
input = sys.stdin.readline

# 연결리스트, 방문체크 테이블, 맥스비용
n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
cost = 1000000001
array = []

# 다리정보 (a와 b사이의 제한이 c다.)
for _ in range(m):
    a, b, limit = map(int, input().split())
    graph[a].append((b, limit))
    graph[b].append((a, limit))
    array.append(limit)
left = min(array)
right = max(array)

# 시작점, 도착점
start, end = map(int, input().split())


# bfs
def bfs(v, limit):
    queue = deque()
    queue.append(v)
    visited = [False] * (n + 1)
    visited[v] = True
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            now = i[0]
            cost = i[1]
            # 다리가 버틸수 있을때
            if cost >= limit:
                # 방문한적이 없으면
                if not visited[now]:
                    visited[now] = True
                    queue.append(now)
                if now == end:
                    return limit


# 이진탐색
result = 0
while left <= right:
    mid = (left + right) // 2
    total = bfs(start, mid)
    # 무게 늘려야함
    if total is not None:
        result = mid
        left = mid + 1
    else:
        right = mid - 1
print(result)