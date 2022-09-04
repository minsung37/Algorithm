# https://school.programmers.co.kr/learn/courses/30/lessons/118666
# 성격 유형 검사하기
from collections import defaultdict


def solution(survey, choices):
    dic = defaultdict(int)
    answer = ''
    for index, item in enumerate(survey):
        score = choices[index]
        if score < 4:
            dic[item[0]] = dic[item[0]] + (4 - score)
        elif score > 4:
            dic[item[1]] = dic[item[1]] + (score - 4)
    if dic["R"] >= dic["T"]:
        answer = answer + "R"
    else:
        answer = answer + "T"

    if dic["C"] >= dic["F"]:
        answer = answer + "C"
    else:
        answer = answer + "F"

    if dic["J"] >= dic["M"]:
        answer = answer + "J"
    else:
        answer = answer + "M"

    if dic["A"] >= dic["N"]:
        answer = answer + "A"
    else:
        answer = answer + "N"

    return answer


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))