# 뉴스 클러스터링
# https://school.programmers.co.kr/learn/courses/30/lessons/17677
from collections import Counter


def solution(str1, str2):

    str1, str2 = str1.upper(), str2.upper()
    str1_list, str2_list = [], []

    for i in range(len(str1) - 1):
        temp = str1[i] + str1[i + 1]
        if str1[i].isalpha() and str1[i + 1].isalpha():
            str1_list.append(temp)

    for i in range(len(str2) - 1):
        temp = str2[i] + str2[i + 1]
        if str2[i].isalpha() and str2[i + 1].isalpha():
            str2_list.append(temp)

    counter1, counter2 = Counter(str1_list), Counter(str2_list)
    inter = len(list((counter1 & counter2).elements()))
    union = len(list((counter1 | counter2).elements()))

    if union == 0 and inter == 0:
        return 65536
    return int(inter / union * 65536)


print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))