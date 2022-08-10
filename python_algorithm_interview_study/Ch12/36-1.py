# https://leetcode.com/problems/combination-sum/
# 180ms 14.1MB
class Solution:
    @staticmethod
    def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
        result, temp = [], []

        def dfs(count, prev):
            if sum(temp[:]) > target:
                return
            if sum(temp[:]) == target:
                result.append(temp[:])
                return
            for i in candidates:
                if i >= prev:
                    temp.append(i)
                    dfs(count + 1, i)
                    temp.pop()
        dfs(0, 0)
        return result


print(Solution.combinationSum([2, 3, 5], 8))