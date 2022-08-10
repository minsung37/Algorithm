# https://leetcode.com/problems/combinations/submissions/
# 2541ms 16.1MB
class Solution:
    @staticmethod
    def combine(n: int, k: int) -> list[list[int]]:
        number, visited, temp, result = [x for x in range(1, n + 1)], [False] * n, [], []

        def dfs(count, num):
            if count == k:
                result.append(temp[:])
                return
            for i in range(n):
                if not visited[i]:
                    temp.append(number[i])
                    for x in range(i + 1):
                        visited[x] = True
                    dfs(count + 1, num + 1)
                    for x in range(i + 1):
                        visited[x] = False
                    temp.pop()
        dfs(0, 0)
        return result


print(Solution.combine(4, 2))