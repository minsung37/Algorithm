import sys
# 블럭제거(pop)2초 블럭놓기(put1)초
# 문제정보 입력받기
n, m, b = map(int, sys.stdin.readline().split())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

mintime, height = 10000000000000, 0
for x in range(257):
    put = 0
    pop = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] < x:
                put = put + x - array[i][j]
            else:
                pop = pop + array[i][j] - x
    brick = pop - put + b
    if brick < 0:
        continue
    time = 2 * pop + put
    if time <= mintime:
        mintime = time
        height = x

print(mintime, height)