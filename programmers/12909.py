# https://school.programmers.co.kr/learn/courses/30/lessons/12909
# 올바른 괄호
def solution(s):
    check = 0
    for i in s:
        if i == "(":
            check = check + 1
        else:
            check = check - 1
        if check < 0:
            return False
    if check == 0:
        return True
    else:
        return False