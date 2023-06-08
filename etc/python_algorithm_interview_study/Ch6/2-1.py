# https://leetcode.com/problems/reverse-string/
# 문자열 뒤집기 - 217ms 8.9MB
class Solution:
    @staticmethod
    def reverseString(s: list[str]) -> None:
        s[:] = s[::-1]
        print(s[:])



