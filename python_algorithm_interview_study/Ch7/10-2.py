# https://leetcode.com/problems/array-partition-i/
# 276ms 16.8MB - 배열 파티션1(책풀이)
class Solution:
    @staticmethod
    def arrayPairSum(nums: list[int]) -> int:
        return sum(sorted(nums)[::2])
