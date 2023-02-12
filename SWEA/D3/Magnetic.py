# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14hwZqABsCFAYD
# 1220. [S/W 문제해결 기본] 5일차 - Magnetic
for t in range(10):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    count = 0
    for col in range(n):
        find_n = False
        for row in range(n):
            if not find_n:
                if graph[row][col] == 1:
                    find_n = True
            else:
                if graph[row][col] == 2:
                    find_n = False
                    count = count + 1
    print("#{} {}".format(t + 1, count))
