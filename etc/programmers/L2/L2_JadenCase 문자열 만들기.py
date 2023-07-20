# JadenCase 문자열 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12951
def solution(s):
    s = s.lower()
    stack = [" "]
    for i in s:
        if stack[-1] == " ":
            stack.append(i.upper())
        else:
            stack.append(i)
    return "".join(stack[1:])



print(solution("3people unFollowed me"))
print(solution("for the last week"))