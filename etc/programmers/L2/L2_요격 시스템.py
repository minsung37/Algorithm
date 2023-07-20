# 요격 시스템
# https://school.programmers.co.kr/learn/courses/30/lessons/181188
def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])
    start, end = targets[0]
    for target in targets[1:]:
        if target[0] >= end:
            answer = answer + 1
            start, end = target
    return answer + 1


print(solution([[4, 8], [4, 5], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]]))
print(solution([[3, 6], [2, 4], [5, 6], [1, 3]]))
print(solution([[5, 10], [6, 8], [8, 9], [0, 4]]))
