# 숫자 카드 나누기
# https://school.programmers.co.kr/learn/courses/30/lessons/135807
import math


def solution(arrayA, arrayB):
    gcd_a, gcd_b = min(arrayA), min(arrayB)
    for i in range(len(arrayA)):
        gcd_a = math.gcd(gcd_a, arrayA[i])
        gcd_b = math.gcd(gcd_b, arrayB[i])

    flag_a, flag_b = True, True
    for i in range(len(arrayA)):
        if arrayA[i] % gcd_b == 0:
            flag_a = False
        if arrayB[i] % gcd_a == 0:
            flag_b = False

    if flag_a or flag_b:
        return max(gcd_a, gcd_b)
    return 0


print(solution([10, 17], [5, 20]))
print(solution([10, 20], [5, 17]))
print(solution([14, 35, 119], [18, 30, 102]))