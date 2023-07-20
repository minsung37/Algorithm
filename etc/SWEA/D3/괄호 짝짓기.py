# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14eWb6AAkCFAYD
# 1218. [S/W 문제해결 기본] 4일차 - 괄호 짝짓기
from collections import defaultdict


for i in range(10):
    n = int(input())
    word = list(input())
    l, r = ["(", "{", "[", "<"], [")", "}", "]", ">"]
    left, right = defaultdict(int), defaultdict(int)
    for j in range(4):
        left[l[j]] = j
        right[r[j]] = j
    stack = []
    while word:
        k = word.pop()
        if stack:
            if stack[-1] in right and k in left:
                if left[k] == right[stack[-1]]:
                    stack.pop()
                    continue
        stack.append(k)
    if stack:
        print("#{} {}".format(i + 1, 0))
    else:
        print("#{} {}".format(i + 1, 1))