# https://leetcode.com/problems/valid-palindrome/
# 유효한 팰린드롬 - 82ms 20.5MB
class Solution:
    @staticmethod
    def isPalindrome(s: str) -> bool:
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                    "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        stack = []
        for x in s:
            x = x.lower()
            if x in alphabet:
                stack.append(x)
        n = len(stack)
        if stack[0:n] == stack[::-1]:
            return True
        else:
            return False
