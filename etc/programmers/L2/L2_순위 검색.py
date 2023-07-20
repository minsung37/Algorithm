# 순위 검색
# https://school.programmers.co.kr/learn/courses/30/lessons/72412
from itertools import combinations
from collections import defaultdict
from bisect import bisect_left


def solution(info, query):
    dic_info = defaultdict(list)
    for idx, resume in enumerate(info):
        temp = resume.split()
        for i in range(5):
            for comb in combinations(temp[:4], i):
                temp_ = "".join(comb)
                dic_info[temp_].append(int(temp[4]))
    for k in dic_info:
        dic_info[k].sort()

    result = []
    for idx, sql in enumerate(query):
        temp = sql.split(" and ")
        temp_ = temp.pop().split()
        for i in temp_:
            temp.append(i)
        while "-" in temp:
            temp.remove("-")
        target_score = int(temp.pop())

        key_query = "".join(temp)
        if key_query in dic_info:
            scores = dic_info[key_query]
            if scores:
                enter = bisect_left(scores, target_score)
                result.append(len(scores) - enter)
        else:
            result.append(0)
    return result


print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))
