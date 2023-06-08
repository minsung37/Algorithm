# https://leetcode.com/problems/product-of-array-except-self/
# 347ms	21MB
class Solution:
    @staticmethod
    def productExceptSelf(nums: list[int]) -> list[int]:
        result, front_product, back_product = [], 1, 1
        # 앞에서 곱하기
        for num in nums:
            result.append(front_product)
            front_product = front_product * num
        # 뒤에서 곱하기
        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * back_product
            back_product = back_product * nums[i]
        return result
