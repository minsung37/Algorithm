# https://leetcode.com/problems/subsets/
# 45ms 14.1MB
class Solution:
    @staticmethod
    def subsets(nums: list[int]) -> list[list[int]]:
        ans = []
        n = len(nums)
        count = 0
        count2 = 0
        for i in range(1 << n):
            tmp = []
            count2 = count2 + 1
            for j in range(n):
                if i & (1 << j):
                    tmp.append(nums[j])
                count = count + 1
            print(tmp)
            ans.append(tmp)
        print(count, count2)
        return ans


print(Solution.subsets([1, 2, 3]))