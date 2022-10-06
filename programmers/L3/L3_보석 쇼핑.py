# 보석 쇼핑
# https://school.programmers.co.kr/learn/courses/30/lessons/67258
from collections import defaultdict


def solution(gems):
    count, last = len(set(gems)), len(gems)
    result, left, right = [0, last], 0, 0

    dic = defaultdict(int)
    dic[gems[0]] = dic[gems[0]] + 1

    while left < last and right < last:
        if len(dic) == count:
            if right - left < result[1] - result[0]:
                result = [left, right]
            else:
                dic[gems[left]] = dic[gems[left]] - 1
                if dic[gems[left]] == 0:
                    del dic[gems[left]]
                left = left + 1
        else:
            right = right + 1
            if right == last:
                break
            dic[gems[right]] = dic[gems[right]] + 1
    return [result[0] + 1, result[1] + 1]



print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))