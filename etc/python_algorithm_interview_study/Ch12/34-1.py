# https://leetcode.com/problems/permutations/
# 40ms 14.3MB
class Solution:
    @staticmethod
    def permute(nums: list[int]) -> list[list[int]]:
        result, temp, visited = [], [], [False] * len(nums)

        def dfs(count):
            # 종료조건
            if count == len(nums):
                # [:] - 값을 복사 해야함
                result.append(temp[:])
                return

            for i in range(len(nums)):
                if not visited[i]:
                    temp.append(nums[i])
                    visited[i] = True
                    dfs(count + 1)
                    visited[i] = False
                    temp.pop()
        dfs(0)
        return result