import copy
import sys
from itertools import combinations
from collections import defaultdict
input = sys.stdin.readline


n, m, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
archer = [x for x in range(m)]
result = 0

# 궁수의 배치
position_list = list(combinations(archer, 3))
for position in position_list:
    kill = 0
    copy_graph = copy.deepcopy(graph)
    for row in range(n - 1, -1, -1):
        archer_kill = defaultdict(list)
        # 각각 궁수에 대해서
        for archer in position:
            for col in range(m):
                for distance in range(d):
                    if row - distance < 0:
                        continue
                    # 거리안에 있는 적을 발견한경우
                    if copy_graph[row - distance][col] == 1 and abs(archer - col) + (distance + 1) <= d:
                        check = distance + abs(archer - col)
                        # 가까우면 업데이트
                        if archer_kill[archer]:
                            if check < archer_kill[archer][0]:
                                archer_kill[archer] = [check, row - distance, col]
                        else:
                            archer_kill[archer] = [check, row - distance, col]
        # 궁수 공격
        for archer in position:
            info = archer_kill[archer]
            if info:
                if copy_graph[info[1]][info[2]] == 1:
                    kill = kill + 1
                    copy_graph[info[1]][info[2]] = 0
    result = max(result, kill)
print(result)