# 숫자 변환하기
# https://school.programmers.co.kr/learn/courses/30/lessons/154538
from collections import deque


def solution(x, y, n):
    queue = deque()
    queue.append([y, 0])
    result = -1
    while queue:
        number, count = queue.popleft()
        if number == x:
            result = count
            break
        if x <= number - n:
            queue.append([number - n, count + 1])
        if x <= number // 2 and number % 2 == 0:
            queue.append([number // 2, count + 1])
        if x <= number // 3 and number % 3 == 0:
            queue.append([number // 3, count + 1])
    return result


print(solution(10, 40, 5))
print(solution(10, 40, 30))
print(solution(2, 5, 4))