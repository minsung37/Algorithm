# https://leetcode.com/problems/two-sum/
# 두수의 합 - 4560ms 14.8MB
class Solution:
    @staticmethod
    def twoSum(nums: list[int], target: int) -> list[int]:
        result = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    result = [i, j]
        return result


print(Solution.twoSum([3, 3], 6))

