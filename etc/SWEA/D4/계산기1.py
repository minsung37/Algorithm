# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14mbSaAEwCFAYD
# 1222. [S/W 문제해결 기본] 6일차 - 계산기1
for t in range(10):
    n = input()
    print("#{} {}".format(t + 1, sum(list(map(int, input().split("+"))))))
