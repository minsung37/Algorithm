# https://school.programmers.co.kr/learn/courses/30/lessons/118667
# 두 큐 합 같게 만들기
from collections import deque


def solution(queue1, queue2):
    target = (sum(queue1) + sum(queue2)) // 2
    count = 0
    first, second = deque(queue1), deque(queue2)
    first_sum, second_sum = sum(first), sum(second)

    while first and second:
        if first_sum == target:
            return count
        elif first_sum > target:
            k = first.popleft()
            first_sum = first_sum - k
        else:
            k = second.popleft()
            first.append(k)
            first_sum = first_sum + k
        count = count + 1
    return -1


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))