# https://leetcode.com/problems/network-delay-time/
# 514ms 16.5MB
import heapq


class Solution:
    @staticmethod
    def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:
        mx = 1000000000
        graph, distance = [[] for _ in range(n + 1)], [mx] * (n + 1)

        for i in times:
            a, b, time = map(int, i)
            graph[a].append((b, time))

        def dijkstra(start):
            q = []
            heapq.heappush(q, (0, start))
            distance[start] = 0
            while q:
                dist, now = heapq.heappop(q)
                if distance[now] < dist:
                    continue
                for i in graph[now]:
                    cost = dist + i[1]
                    if cost < distance[i[0]]:
                        distance[i[0]] = cost
                        heapq.heappush(q, (cost, i[0]))
        dijkstra(k)
        result = max(distance[1:])
        if result == mx:
            result = -1
        return result