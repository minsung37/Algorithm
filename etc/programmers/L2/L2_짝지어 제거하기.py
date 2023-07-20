# https://programmers.co.kr/learn/courses/30/lessons/12973
# 짝지어 제거하기
def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        else:
            if i == stack[-1]:
                stack.pop()
                continue
            stack.append(i)
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0
    return answer