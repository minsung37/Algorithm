# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 67ms 14MB
class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        dic, start, answer = {}, 0, 0
        for value, key in enumerate(s):
            if key in dic:
                start = max(start, dic[key] + 1)
            dic[key] = value
            answer = max(answer, value - start + 1)
        return answer