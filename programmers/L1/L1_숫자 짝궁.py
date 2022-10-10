# 숫자 짝꿍
# https://school.programmers.co.kr/learn/courses/30/lessons/131128?language=python3
from collections import defaultdict


def solution(X, Y):
    dic_x, dic_y = defaultdict(int), defaultdict(int)
    for i in range(10):
        dic_x[i] = X.count(str(i))
        dic_y[i] = Y.count(str(i))

    result = ""
    for i in range(9, -1, -1):
        k = min(dic_y[i], dic_x[i])
        result = result + str(i) * k

    if len(result) == 0:
        return "-1"
    elif list(set(result)) == ['0']:
        return "0"
    else:
        return result


print(solution("100", "2345"))
print(solution("100", "203045"))
print(solution("100", "123450"))
print(solution("12321", "42531"))
print(solution("5525", "1255"))