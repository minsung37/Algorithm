# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# 37ms 13.9MB
from itertools import product


class Solution:
    @staticmethod
    def letterCombinations(digits: str) -> list[str]:
        number = [0, 0, ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], ["m", "n", "o"],
                  ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]
        temp = []
        if digits is None:
            return temp
        for i in digits:
            temp.append(number[int(i)])
        result = list(product(*temp))
        for i in range(len(result)):
            result[i] = "".join(result[i])
        return result