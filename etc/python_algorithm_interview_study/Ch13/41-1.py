# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# 216ms 15.5MB
import heapq


class Solution:
    @staticmethod
    def findCheapestPrice(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph, q, visited = [[] for _ in range(n + 1)], [(0, src, k)], {}
        for a, b, cost in flights:
            graph[a].append((b, cost))

        while q:
            cost, now, k = heapq.heappop(q)
            if now == dst:
                return cost
            if k >= 0:
                # 방문안했거나 남은 곳의 개수가 더크면 k값 초기화
                if now not in visited or visited[now] < k:
                    visited[now] = k
                    for now_, cost_ in graph[now]:
                        heapq.heappush(q, (cost + cost_, now_, k - 1))
        return -1


print(Solution.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0))