# https://leetcode.com/problems/jewels-and-stones/
# 31ms 13.9MB
class Solution:
    @staticmethod
    def numJewelsInStones(jewels: str, stones: str) -> int:
        count = 0
        for j in jewels:
            count = count + stones.count(j)
        return count