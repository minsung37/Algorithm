# https://leetcode.com/problems/course-schedule/
# 134ms 17.6MB
import collections


class Solution:
    @staticmethod
    def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)
        # 순환체크, 방문체크
        traced, visited = set(), set()

        def dfs(i):
            if i in traced:
                return False
            if i in visited:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            # 순환노드 삭제
            traced.remove(i)
            # 방문체크
            visited.add(i)
            return True

        for x in list(graph):
            if not dfs(x):
                return False
        return True