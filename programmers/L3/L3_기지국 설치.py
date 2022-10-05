# 기지국 설치
# https://school.programmers.co.kr/learn/courses/30/lessons/12979
import math


def solution(n, stations, w):
    answer = 0
    distance = [(0, 0)]
    for s in stations:
        if s - w >= 0:
            left = s - w
        else:
            left = 0
        if s + w < n:
            right = s + w
        else:
            right = n
        distance.append((left, right))
    distance.append((n + 1, n + 1))

    for i in range(len(distance) - 1):
        answer = answer + math.ceil((distance[i + 1][0] - (distance[i][1] + 1)) / (2 * w + 1))

    return answer


print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))