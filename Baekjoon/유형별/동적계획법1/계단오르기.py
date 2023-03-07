# 계단개수 입력받기
n = int(input())

# 계단 입력받기
stairs = [0]
for i in range(n):
    a = int(input())
    stairs.append(a)

# 1일때 예외처리
if n == 1:
    print(stairs[1])
else:
    # n번째 올랐을때 점수
    d = [0] * (n + 1)
    d[1] = stairs[1]
    d[2] = d[1] + stairs[2]

    # 계단오르기
    for i in range(3, n + 1):
        d[i] = max(d[i - 2], d[i - 3] + stairs[i - 1]) + stairs[i]

    # 결과출력
    print(d[n])