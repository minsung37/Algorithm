# https://leetcode.com/problems/two-sum/
# 두수의 합 - 1009ms 15MB
class Solution:
    @staticmethod
    def twoSum(nums: list[int], target: int) -> list[int]:
        result = []
        for num_index in range(len(nums)):
            another_num = target - nums[num_index]
            nums[num_index] = 10 ** 9 + 1
            if another_num in nums:
                another_num_index = nums.index(another_num)
                result.append(num_index)
                result.append(another_num_index)
                return result