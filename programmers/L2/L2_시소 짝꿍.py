# 시소 짝궁
# https://school.programmers.co.kr/learn/courses/30/lessons/152996
from collections import defaultdict


def solution(weights):
    result = 0
    dic = defaultdict(int)
    for w in weights:
        result = result + dic[w] + dic[w / 2] + dic[w * 2] + dic[(w * 3) / 2] + dic[(w * 4) / 3] + dic[(w * 2) / 3] + dic[(w * 3) / 4]
        dic[w] = dic[w] + 1
    return result


print(solution([100, 180, 360, 100, 270]))
