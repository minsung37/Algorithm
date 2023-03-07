from collections import defaultdict
from collections import deque
import sys
input = sys.stdin.readline


def bfs(v):
    queue = deque()
    queue.append([v, 0])
    visited = [False] * (n + 1)
    visited[v] = True
    while queue:
        x, length = queue.popleft()
        visited[x] = True
        distance[x] = length
        for node, cost in tree[x]:
            if not visited[node]:
                visited[node] = True
                queue.append([node, length + cost])


n = int(input())
tree = defaultdict(list)
for _ in range(n - 1):
    parent, child, cost = map(int, input().split())
    tree[parent].append([child, cost])
    tree[child].append([parent, cost])


distance = [0] * (n + 1)
# 1번 노드에서 가장먼점은 지름의 양끝 점중 하나임
bfs(1)
bfs(distance.index(max(distance)))
print(max(distance))