from collections import defaultdict
from collections import deque
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
snake_and_ladder = defaultdict(int)
visited = [False] * 101
for _ in range(n + m):
    x, y = map(int, input().split())
    snake_and_ladder[x] = y
queue = deque()
queue.append([1, 0])
visited[1] = True
while queue:
    x, count = queue.popleft()
    if x == 100:
        print(count)
        break
    for i in range(1, 7):
        nx = x + i
        if nx > 100:
            continue
        if visited[nx]:
            continue
        # 범위 안에 있고 방문 한적 없는경우, 뱀과 사다리가 있는경우
        if snake_and_ladder[nx] != 0:
            nx = snake_and_ladder[nx]
        queue.append([nx, count + 1])
        visited[nx] = True