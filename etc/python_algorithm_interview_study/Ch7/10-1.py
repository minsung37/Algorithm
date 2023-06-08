# https://leetcode.com/problems/array-partition-i/
# 356ms 16.6MB - 배열 파티션1
class Solution:
    @staticmethod
    def arrayPairSum(nums: list[int]) -> int:
        nums.sort()
        result, n = 0, len(nums) // 2
        for i in range(n):
            result = result + nums[i * 2]
        return result
