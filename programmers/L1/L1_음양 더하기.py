# 음양 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/76501
def solution(absolutes, signs):
    result = 0
    for idx, sign in enumerate(signs):
        if sign:
            result = result + absolutes[idx]
        else:
            result = result - absolutes[idx]
    return result