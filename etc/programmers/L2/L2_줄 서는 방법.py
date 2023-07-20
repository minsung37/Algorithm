# 줄 서는 방법
# https://school.programmers.co.kr/learn/courses/30/lessons/12936
import math


def solution(n, k):
    people, result = [x for x in range(1, n + 1)], []
    k = k - 1

    while people:
        index = k // math.factorial(n - 1)
        number = people[index]
        result.append(number)
        people.remove(number)

        k = k % math.factorial(n - 1)
        n = n - 1

    return result


print(solution(3, 5))