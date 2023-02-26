from collections import deque
import sys
input = sys.stdin.readline


n = int(input())
dslr_dic = {0: "D", 1: "S", 2: "L", 3: "R"}
for i in range(n):
    start, target = map(int, input().split())
    visited = [False] * 10000
    queue = deque()
    queue.append([start, ""])
    visited[start] = True
    DSLR = [0] * 4
    while queue:
        x, commend = queue.popleft()
        if x == target:
            print(commend)
            break
        DSLR[0] = (2 * x) % 10000
        DSLR[1] = (x - 1) % 10000
        DSLR[2] = (10 * x + (x // 1000)) % 10000
        DSLR[3] = (x // 10 + (x % 10) * 1000) % 10000
        for index, value in enumerate(DSLR):
            if not visited[value]:
                visited[value] = True
                queue.append([value, commend + dslr_dic[index]])