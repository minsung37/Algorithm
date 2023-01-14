from collections import deque
import sys
input = sys.stdin.readline


n, k = map(int, input().split())
limit = 100001
dp = [-1] * limit
dp[n] = 0
if n == k:
    print(0)
    exit(0)
queue = deque()
queue.append([n, 0])
while queue:
    v, t = queue.popleft()
    next_v = [[2 * v, t], [v - 1, t + 1], [v + 1, t + 1]]
    if v == k:
        print(dp[v])
        break
    for n, time in next_v:
        if 0 <= n < limit:
            if dp[n] == -1 or time < dp[n]:
                dp[n] = time
                if t == time:
                    queue.appendleft([n, time])
                else:
                    queue.append([n, time])
