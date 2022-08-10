# https://leetcode.com/problems/top-k-frequent-elements/
# 101ms 18.7MB
class Solution:
    @staticmethod
    def topKFrequent(nums: list[int], k: int) -> list[int]:
        dic, result = {}, []
        for i in nums:
            if i in dic:
                dic[i] = dic[i] + 1
            else:
                dic[i] = 1
        order = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        for x, y in order:
            if len(result) == k:
                break
            result.append(x)
        return sorted(result)