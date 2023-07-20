# 두 원 사이의 정수 쌍
# https://school.programmers.co.kr/learn/courses/30/lessons/181187
import math


def solution(r1, r2):
    answer = 0
    # 1사분면과 x > 0 일때 x축 상에 위치한 점
    for x in range(1, r2 + 1):
        y1 = (r1 ** 2 - x ** 2)
        if y1 <= 0:
            y1 = 0
        else:
            y1 = math.ceil(y1 ** 0.5)
        y2 = math.floor((r2 ** 2 - x ** 2) ** 0.5)
        answer = answer + (y2 - y1 + 1)
    return answer * 4


print(solution(2, 3))

