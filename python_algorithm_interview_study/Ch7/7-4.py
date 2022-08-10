# https://leetcode.com/problems/two-sum/
# 두수의 합 - 67ms 15.2MB(책풀이4번) - 조회 구조 개선
class Solution:
    @staticmethod
    def twoSum(nums: list[int], target: int) -> list[int]:
        nums_map = {}
        # 하나의 for 문으로 통합
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i