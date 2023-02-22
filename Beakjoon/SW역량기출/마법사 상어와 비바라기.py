import sys
input = sys.stdin.readline


n, m = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]
magic = [list(map(int, input().split())) for _ in range(m)]
#        ←   ↖   ↑   ↗  →  ↘  ↓  ↙
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
cloud = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]
for d, s in magic:
    # 비온곳 체크
    visited = [[False] * n for _ in range(n)]
    for index, value in enumerate(cloud):
        # 구름이동
        value[0] = (value[0] + dx[d] * s) % n
        value[1] = (value[1] + dy[d] * s) % n
        cloud[index] = value
    # 비내리기
    for x, y in cloud:
        ground[x][y] = ground[x][y] + 1
        visited[x][y] = True
    # 물복사
    for x, y in cloud:
        water = 0
        for v in range(2, 9, 2):
            nx = x + dx[v]
            ny = y + dy[v]
            if 0 <= nx < n and 0 <= ny < n:
                if ground[nx][ny] > 0:
                    water = water + 1
        ground[x][y] = ground[x][y] + water
    # 두번째 구름생성
    new_cloud = []
    for x in range(n):
        for y in range(n):
            if not visited[x][y] and ground[x][y] >= 2:
                ground[x][y] = ground[x][y] - 2
                new_cloud.append([x, y])
    cloud = new_cloud
# 결과 출력
result = 0
for i in ground:
    result = result + sum(i)
print(result)