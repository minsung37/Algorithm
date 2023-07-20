# https://school.programmers.co.kr/learn/courses/30/lessons/12977
# 소수 만들기
from itertools import combinations
import math


def solution(nums):
    result = 0
    comb = list(combinations(nums, 3))
    eratos = [True for _ in range(3000)]
    eratos[0], eratos[1] = False, False

    for i in range(2, int(math.sqrt(len(eratos)) + 1)):
        if eratos[i]:
            for j in range(i + i, len(eratos), i):
                eratos[j] = False

    for i in comb:
        k = sum(i)
        if eratos[k]:
            result = result + 1
    return result


print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))