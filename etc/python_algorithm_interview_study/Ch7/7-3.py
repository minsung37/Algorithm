# https://leetcode.com/problems/two-sum/
# 두수의 합 - 64ms 15MB(책풀이3번) - 첫 번째 수를 뺸 결과 키 조회
class Solution:
    @staticmethod
    def twoSum(nums: list[int], target: int) -> list[int]:
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]



