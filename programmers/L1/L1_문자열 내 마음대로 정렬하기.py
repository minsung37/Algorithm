# https://school.programmers.co.kr/learn/courses/30/lessons/12915
# 문자열 내 마음대로 정렬하기
from collections import defaultdict


def solution(strings, n):
    dic = defaultdict(list)
    result = []

    for string in strings:
        dic[string[n]].append(string)
    for i in dic:
        dic[i] = sorted(dic[i])

    items = sorted(dic.items())
    for item in items:
        for i in item[1]:
            result.append(i)

    return result


print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))