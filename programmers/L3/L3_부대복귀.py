from collections import defaultdict
from collections import deque


def solution(n, roads, sources, destination):
    def bfs(target):
        q = deque()
        q.append([0, target])
        dp[destination] = 0
        while q:
            cost, curr = q.popleft()
            for v in graph[curr]:
                if dp[v] == int(1e9):
                    q.append([cost + 1, v])
                    dp[v] = cost + 1

    graph = defaultdict(list)
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    dp = [int(1e9)] * (n + 1)
    bfs(destination)
    result = [dp[x] if dp[x] != int(1e9) else -1 for x in sources]
    return result


print(solution(3, [[1, 2], [2, 3]], [2, 3], 1))
print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))