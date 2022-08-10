# https://leetcode.com/problems/remove-duplicate-letters/
# 38ms 13.9MB
import collections


class Solution:
    @staticmethod
    def removeDuplicateLetters(s: str) -> str:
        # {'c': 4, 'b': 2, 'a': 1, 'd': 1} 이렇게 문자열을 나타낸다
        counter = collections.Counter(s)
        stack = []
        for char in s:
            counter[char] = counter[char] - 1
            if char in stack:
                continue
            # 스택[-1]이 더크고 s에 char가 두개 이상있을때 그 문자를 pop한다
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(char)
        return ''.join(stack)



print(Solution.removeDuplicateLetters("cbacdcbc"))
print(Solution.removeDuplicateLetters("bcabc"))