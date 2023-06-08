# https://leetcode.com/problems/valid-parentheses/
# 32ms 13.9MB
class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        parenthesis = [[")", "("], ["}", "{"], ["]", "["]]
        s, stack = list(s), []
        while s:
            # s에서 하나씩 빼서 스택에 넣기
            stack.append(s.pop())
            # 스택 뒤 2개가 괄호열이면 2개를 스택에서 팝한다.
            if stack[-2:] in parenthesis:
                stack.pop()
                stack.pop()
        # 전부 pop된경우에는 stack의 길이가 0이다
        if len(stack) == 0:
            return True
        return False