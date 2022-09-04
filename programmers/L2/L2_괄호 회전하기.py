# https://programmers.co.kr/learn/courses/30/lessons/76502
# 괄호 회전하기
def check(s):
    target = [")(", "][", "}{"]
    s = list(s)
    stack = ""
    if len(s) == 0:
        return 0
    k = s.pop()
    if len(stack) == 0:
        if k in ["(", "[", "{"]:
            return False
        stack = stack + k
    while s:
        k = s.pop()
        stack = stack + k
        for i in target:
            if i in stack:
                stack = stack.replace(i, "")
                break
    if len(stack) == 0:
        return True
    else:
        return False


def solution(s):
    answer = 0
    for _ in range(len(s)):
        if check(s):
            answer = answer + 1
        s = s + s[0]
        s = s[1:]
    return answer


print(solution("[](){}"))