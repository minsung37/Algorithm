# https://school.programmers.co.kr/learn/courses/30/lessons/12921
# 소수 찾기
import math


def solution(n):
    eratos = [True for _ in range(n + 1)]
    eratos[0], eratos[1] = False, False

    for i in range(2, int(math.sqrt(len(eratos)) + 1)):
        if eratos[i]:
            for j in range(i + i, len(eratos), i):
                eratos[j] = False
    answer = eratos.count(True)
    return answer


print(solution(10))
print(solution(5))