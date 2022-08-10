# https://leetcode.com/problems/subsets/
# 51ms 14.1MB
class Solution:
    @staticmethod
    def subsets(nums: list[int]) -> list[list[int]]:
        result, temp = [], []

        def dfs(count, prev):
            comb = sorted(temp[:])
            result.append(comb)
            if count == len(nums):
                return
            for i in nums:
                if i > prev:
                    temp.append(i)
                    dfs(count + 1, i)
                    temp.pop()
        dfs(0, -11)
        return result