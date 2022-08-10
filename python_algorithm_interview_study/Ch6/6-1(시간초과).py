# https://leetcode.com/problems/longest-palindromic-substring/
# 가장 긴 팰린드롬 부분 문자열
class Solution:
    @staticmethod
    def longestPalindrome(s: str) -> str:
        palindrome = []
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                word = s[i:j]
                if word == word[::-1]:
                    palindrome.append(word)
        return max(palindrome, key=len)


Solution.longestPalindrome("babad")
