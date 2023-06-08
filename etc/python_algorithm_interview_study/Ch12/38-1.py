# https://leetcode.com/problems/reconstruct-itinerary/
# 117ms 14.3MB
import collections


class Solution:
    @staticmethod
    def findItinerary(tickets: list[list[str]]) -> list[str]:
        tickets, result = sorted(tickets, reverse=True), []
        schedule = collections.defaultdict(list)
        for start, end in tickets:
            schedule[start].append(end)

        def dfs(next):
            while schedule[next]:
                dfs(schedule[next].pop())
            result.append(next)
        dfs('JFK')
        return result[::-1]


print(Solution.findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]))