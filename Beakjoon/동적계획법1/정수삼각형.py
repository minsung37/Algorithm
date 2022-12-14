# 삼각형의 높이 입력받기
n = int(input())

# 삼각형 입력받기
angle = []
for i in range(n):
    a = list(map(int, input().split()))
    angle.append(a)

# 계산
for i in range(n - 1):
    # 수열의 상단 더하기
    for j in range(len(angle[i + 1])):
        # j == 0 이면 가장 앞의 성분이 더해짐
        if j == 0:
            angle[i + 1][j] = angle[i + 1][j] + angle[i][0]
        # j != 0 이면 j-1 or j 중 큰값이 더해짐
        else:
            angle[i + 1][j] = angle[i + 1][j] + max(angle[i][j-1:j+1])

# 정답 출력
print(max(angle[n - 1]))