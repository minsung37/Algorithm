# https://leetcode.com/problems/3sum/
# 7253ms 18.1MB - 세 수의 합
class Solution:
    @staticmethod
    def threeSum(nums: list[int]) -> list[list[int]]:
        result, n = [], len(nums) - 1
        nums.sort()
        for i in range(n):
            first, left, right = nums[i], i + 1, n
            while left <= right:
                second, third = nums[left], nums[right]
                three_sum = first + second + third
                if three_sum == 0:
                    temp = [first, second, third]
                    if temp not in result and left != right:
                        result.append(temp)
                if three_sum >= 0:
                    right = right - 1
                if three_sum < 0:
                    left = left + 1
        return result

