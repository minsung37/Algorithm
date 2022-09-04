# https://school.programmers.co.kr/learn/courses/30/lessons/86971
# 전력망을 둘로 나누기
import collections
from collections import deque


def solution(n, wires):
    result = []
    for i in range(len(wires)):
        wire = collections.defaultdict(list)
        count = set()
        visited = [False] * (n + 1)
        for x in wires:
            if x != wires[i]:
                wire[x[0]].append(x[1])
                wire[x[1]].append(x[0])
        queue = deque()
        queue.append(1)
        while queue:
            v = queue.popleft()
            visited[v] = True
            count.add(v)
            for k in wire[v]:
                if not visited[k]:
                    queue.append(k)
        result.append(abs((n - len(count)) - len(count)))
    return min(result)


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
print(solution(4, [[1, 2], [2, 3], [3, 4]]))
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))