import copy
from collections import deque
from itertools import permutations
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
matrix_original = [list(map(int, input().split())) for _ in range(n)]
rotation_list = [list(map(int, input().split())) for _ in range(k)]
rotation_comb = list(permutations(rotation_list, k))
result = 1000000000
for rotations in rotation_comb:
    matrix = copy.deepcopy(matrix_original)
    for rotation in rotations:
        r, c, s = rotation
        ltx, lty = r - s - 1, c - s - 1     # 좌상단 x, y
        rdx, rdy = r + s - 1, c + s - 1     # 우하단 x, y
        repeat = (rdx - ltx + 1) // 2
        for _ in range(repeat):
            queue = deque()
            for i in range(lty, rdy):
                queue.append([ltx, i, matrix[ltx][i]])
            for i in range(ltx, rdx):
                queue.append([i, rdy, matrix[i][rdy]])
            for i in range(rdy, lty, -1):
                queue.append([rdx, i, matrix[rdx][i]])
            for i in range(rdx, ltx, -1):
                queue.append([i, lty, matrix[i][lty]])
            after = copy.deepcopy(queue)
            queue.append(queue.popleft())
            ltx, lty = ltx + 1, lty + 1
            rdx, rdy = rdx - 1, rdy - 1
            while queue:
                x, y, value1 = queue.popleft()
                p, q, value2 = after.popleft()
                matrix[x][y] = value2
    for i in matrix:
        result = min(result, sum(i))
print(result)