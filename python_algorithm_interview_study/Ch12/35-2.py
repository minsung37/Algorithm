# https://leetcode.com/problems/combinations/submissions/
# 514ms 16MB
class Solution:
    @staticmethod
    def combine(n: int, k: int) -> list[list[int]]:
        result, temp = [], []

        def dfs(count, num):
            if count == k:
                result.append(temp[:])
                return
            for i in range(num, n + 1):
                temp.append(i)
                dfs(count + 1, i + 1)
                temp.pop()
        dfs(0, 1)
        return result


print(Solution.combine(4, 2))