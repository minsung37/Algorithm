# https://school.programmers.co.kr/learn/courses/30/lessons/92334
# 신고 결과 받기
from collections import defaultdict


def solution(id_list, report, k):
    dic = defaultdict(int)
    get_mail = defaultdict(list)
    report = list(set(report))

    for info in report:
        temp = info.split()
        dic[temp[1]] = dic[temp[1]] + 1
        get_mail[temp[1]].append(temp[0])

    stop = []
    for i in id_list:
        if dic[i] >= k:
            stop.append(i)

    result = [0] * len(id_list)
    for index, i in enumerate(id_list):
        for j in stop:
            if i in get_mail[j]:
                result[index] = result[index] + 1

    return result


print(
    solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
             2))
print(solution(["con", "ryan"],	["ryan con", "ryan con", "ryan con", "ryan con"], 3))