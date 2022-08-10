# 집의수 입력받기
n = int(input())

# rgb값 입력받기
rgb = []
for i in range(n):
    a = list(map(int, input().split()))
    rgb.append(a)

# 계산
for i in range(1, n):
    # 2번쨰 집이 R인경우 이전집의 G,B 값중 작은걸 더함
    rgb[i][0] = min(rgb[i - 1][1], rgb[i - 1][2]) + rgb[i][0]
    # 2번쨰 집이 G인경우 이전집의 R,B 값중 작은걸 더함
    rgb[i][1] = min(rgb[i - 1][0], rgb[i - 1][2]) + rgb[i][1]
    # 2번쨰 집이 B인경우 이전집의 R,G 값중 작은걸 더함
    rgb[i][2] = min(rgb[i - 1][0], rgb[i - 1][1]) + rgb[i][2]

# 정답 출력
print(min(rgb[n - 1]))