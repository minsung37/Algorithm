# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AYZYZIsKIzIDFARc
# 16603. 2차원 배열 테두리 회전
import copy
from collections import deque

T = int(input())
for t in range(T):
    tc = input()
    n, m, k = map(int, input().split())
    squre = [list(map(int, input().split())) for _ in range(n)]

    queue = deque()
    for i in range(m - 1):
        queue.append([0, i])
    for i in range(n - 1):
        queue.append([i, m - 1])
    for i in range(m - 1):
        queue.append([n - 1, m - 1 - i])
    for i in range(n - 1):
        queue.append([n - 1 - i, 0])

    after_queue = copy.deepcopy(queue)
    for _ in range(k):
        after_queue.append(after_queue.popleft())

    new_squre = copy.deepcopy(squre)
    for after, before in zip(after_queue, queue):
        new_squre[after[0]][after[1]] = squre[before[0]][before[1]]

    print("#" + tc)
    for i in new_squre:
        print(*i)