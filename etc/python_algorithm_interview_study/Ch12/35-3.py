# https://leetcode.com/problems/combinations/submissions/
# 106ms 15.9MB
import itertools


class Solution:
    @staticmethod
    def combine(n: int, k: int) -> list[list[int]]:
        return list(itertools.combinations(range(1, n+1), k))


print(Solution.combine(4, 2))