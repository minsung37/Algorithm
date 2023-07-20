# https://school.programmers.co.kr/learn/courses/30/lessons/42889
# 실패율
from collections import defaultdict


def solution(N, stages):
    user, result, dic = 0, [], {}

    info = defaultdict(int)
    for stage in stages:
        if stage <= N:
            info[stage] = info[stage] + 1

    for i in range(1, N + 1):
        k = info[i]
        if k == 0:
            dic[i] = 0
        else:
            dic[i] = k / (len(stages) - user)
        user = user + k

    temp = sorted(dic.items(), key=lambda x: x[1], reverse=True)

    for i in temp:
        result.append(i[0])
    return result


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
