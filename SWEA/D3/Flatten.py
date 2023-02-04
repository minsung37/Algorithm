# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV139KOaABgCFAYh
# 1208. [S/W 문제해결 기본] 1일차 - Flatten
for t in range(10):
    flatten = int(input())
    ground = list(map(int, input().split()))
    # 최대 최소의 인덱스를 구하고 1씩 증감 반복
    for _ in range(flatten):
        take, down = max(ground), min(ground)
        take_idx, down_idx = ground.index(take), ground.index(down)
        ground[take_idx], ground[down_idx] = ground[take_idx] - 1, ground[down_idx] + 1
    print("#{} {}".format(t + 1, max(ground) - min(ground)))