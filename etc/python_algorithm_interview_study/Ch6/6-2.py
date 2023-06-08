# https://leetcode.com/problems/longest-palindromic-substring/
# 가장 긴 팰린드롬 부분 문자열 - 306ms 14MB(책풀이)
# 시간초과나서 책풀이보고 풀었습니다. ㅜㅜ
class Solution:
    @staticmethod
    def longestPalindrome(s: str) -> str:

        # 팰린드롬 판별 및 투포인터 확장
        def expand(left, right):
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                left = left - 1
                right = right + 1
            return s[left + 1:right - 1]

        # 해당 사항이 없을 때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s

        # 슬라이딩 윈도우 우측으로 이동
        result = ''
        for i in range(len(s) - 1):
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
            print(result)
        return result


print(Solution.longestPalindrome("babad"))
