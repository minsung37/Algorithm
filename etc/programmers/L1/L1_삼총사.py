# 삼총사
# https://school.programmers.co.kr/learn/courses/30/lessons/131705
from itertools import combinations


def solution(number):
    temp = []
    answer = 0
    for i in range(len(number)):
        temp.append(i)
    combs = list(combinations(temp, 3))
    for comb in combs:
        check = 0
        for i in comb:
            check = check + number[i]
        if check == 0:
            answer = answer + 1
    return answer


print(solution([-2, 3, 0, 2, -5]))
print(solution([-3, -2, -1, 0, 1, 2, 3]))
print(solution([-1, 1, -1, 1]))