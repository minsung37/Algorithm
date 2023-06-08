# https://leetcode.com/problems/3sum/
# 796ms 18.1MB - 세 수의 합(책풀이)
class Solution:
    @staticmethod
    def threeSum(nums: list[int]) -> list[list[int]]:
        result, length = [], len(nums)
        nums.sort()
        for i in range(length - 2):
            # 중복된값 건너뛰기
            if nums[i] > 0 or (i > 0 and nums[i] == nums[i - 1]):
                continue
            # 간격을 좁혀가며 합 sum 계산
            left, right = i + 1, length - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum < 0:
                    left = left + 1
                elif three_sum > 0:
                    right = right - 1
                else:
                    # 세수의합 0 인경우
                    result.append((nums[i], nums[left], nums[right]))
                    # 지금수와 다음수가 같을때 스킵처리
                    while left < right and nums[left] == nums[left + 1]:
                        left = left + 1
                    while left < right and nums[right] == nums[right - 1]:
                        right = right - 1
                    # 다른거 부터 합을 구하도록
                    left = left + 1
                    right = right - 1
        return result