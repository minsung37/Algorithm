# https://school.programmers.co.kr/learn/courses/30/lessons/42892
# 길 찾기 게임
from collections import defaultdict


def solution(nodeinfo):
    answer = [[]]
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))
    dic = defaultdict([0, 0])
    parent = 0
    child = []
    for x, y in range(nodeinfo):
        if parent == 0:
            parent = x

    return answer


print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
print(solution([[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]]))
