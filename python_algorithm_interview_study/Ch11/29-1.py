# https://leetcode.com/problems/jewels-and-stones/
# 29ms 13.8MB
class Solution:
    @staticmethod
    def numJewelsInStones(jewels: str, stones: str) -> int:
        jewels, stones, count = list(set(jewels)), list(stones), 0
        for i in jewels:
            for j in stones:
                if i == j:
                    count = count + 1
        return count