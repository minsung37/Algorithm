# 뒤에 있는 큰 수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/154539
from collections import deque


def solution(numbers):
    queue = deque()
    queue.append(numbers.pop())
    answer = [-1]
    while numbers:
        k = numbers.pop()
        queue2 = deque()
        check = False
        for num in queue:
            if k < num:
                if not check:
                    answer.append(num)
                    check = True
                queue2.append(num)
        if not check:
            answer.append(-1)
        queue2.appendleft(k)
        queue = queue2
    answer.reverse()
    return answer


print(solution([2, 3, 3, 5]))
print(solution([9, 1, 5, 3, 6, 2]))