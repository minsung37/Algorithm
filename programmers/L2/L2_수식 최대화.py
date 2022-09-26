# 수식 최대화
# https://school.programmers.co.kr/learn/courses/30/lessons/67257
from collections import defaultdict
from itertools import permutations


def solution(expression):
    expression = expression.replace("-", "^")
    mark = ["^", "*", "+"]
    number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]
    dic = defaultdict(int)
    for i in expression:
        if i in mark:
            dic[i] = dic[i] + 1

    def cal(calculation):
        check = False
        first, second = "", ""
        for num in value:
            if check:
                if num in number:
                    second = second + num
                else:
                    break
            if not check:
                if num in number:
                    first = first + num
                else:
                    if num == calculation:
                        check = True
                    else:
                        first = ""
        if second == "":
            return value.replace(first, str(int(first)))
        if calculation == "^":
            return value.replace(first + "^" + second, str(int(first) - int(second)))
        if calculation == "+":
            return value.replace(first + "+" + second, str(int(first) + int(second)))
        if calculation == "*":
            return value.replace(first + "*" + second, str(int(first) * int(second)))

    result = []
    calculate = list(permutations(mark, 3))
    for i in calculate:
        value = expression
        for j in i:
            for _ in range(dic[j]):
                value = cal(j)
        result.append(abs(int(value)))
    return max(result)


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))