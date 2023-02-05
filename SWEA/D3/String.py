# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14P0c6AAUCFAYi
# 1213. [S/W 문제해결 기본] 3일차 - String
for _ in range(10):
    n, target, sentence, result = int(input()), list(input()), list(input()), 0
    for i in range(len(sentence) - len(target) + 1):
        if target == sentence[i: i + len(target)]:
            result = result + 1
    print("#{} {}".format(n, result))
