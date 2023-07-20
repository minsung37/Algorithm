# 게리맨더링
# https://www.acmicpc.net/problem/17471
from collections import defaultdict
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
city = [x for x in range(1, n + 1)]
population = list(map(int, input().split()))
graph = defaultdict(set)
for i in range(1, n + 1):
    info = list(map(int, input().split()))
    for j in info[1:]:
        graph[j].add(i)
        graph[i].add(j)
a_party = []
result = int(1e9)


def combination(index):
    if 1 <= len(a_party) <= n // 2:
        garrymendering(a_party)
    for i in range(index, n + 1):
        a_party.append(i)
        combination(i + 1)
        a_party.pop()


def garrymendering(a_party):
    global result
    b_party = [x for x in range(1, n + 1) if x not in a_party]
    a_set, b_set = set(a_party), set(b_party)
    a_check, b_check = set(), set()

    a_queue = deque()
    a_queue.append(a_party[0])
    a_check.add(a_party[0])

    b_queue = deque()
    b_queue.append(b_party[0])
    b_check.add(b_party[0])

    while a_queue:
        x = a_queue.popleft()
        for v in graph[x]:
            if v in b_set or v in a_check:
                continue
            a_queue.append(v)
            a_check.add(v)
    while b_queue:
        x = b_queue.popleft()
        for v in graph[x]:
            if v in a_set or v in b_check:
                continue
            b_queue.append(v)
            b_check.add(v)
    is_garrymendering = len(a_check) + len(b_check)
    if is_garrymendering == n:
        a, b = 0, 0
        for i in a_party:
            a = a + population[i - 1]
        for i in b_party:
            b = b + population[i - 1]
        if abs(a - b) < result:
            result = abs(a - b)


combination(1)
if result == int(1e9):
    result = -1
print(result)