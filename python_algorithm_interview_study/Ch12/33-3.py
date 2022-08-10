# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# 31ms 14MB
class Solution:
    @staticmethod
    def letterCombinations(digits: str) -> list[str]:
        number = [0, 0, ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], ["m", "n", "o"],
                  ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]
        temp, result, count = [], [], 0
        if len(digits) == 0:
            return temp

        def dfs(count):
            # 종료조건
            if count == len(digits):
                result.append("".join(temp))
                return
            dial = number[int(digits[count])]
            for j in dial:
                temp.append(j)
                dfs(count + 1)
                temp.pop()
        dfs(0)
        return result