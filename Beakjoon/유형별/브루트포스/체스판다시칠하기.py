# 체스판 입력받기
n, m = map(int, input().split())
chess = []
target = []
for _ in range(n):
    chess.append(input())

# 검사
for a in range(n - 7):
    for i in range(m - 7):
        x = 0
        y = 0
        # 8X8 범위를 B와 W로 번갈아가면서 검사
        for b in range(a, a + 8):
            for j in range(i, i + 8):
                # 인덱스 합이 짝수인경우
                if (j + b) % 2 == 0:
                    if chess[b][j] == 'W':
                        x += 1
                    if chess[b][j] == 'B':
                        y += 1
                # 인덱스 합이 홀수인경우
                else:
                    if chess[b][j] == 'B':
                        x += 1
                    if chess[b][j] == 'W':
                        y += 1
        # W로 시작했을 때 칠해야 할 부분
        target.append(x)
        # B로 시작했을 때 칠해야 할 부분
        target.append(y)

# 칠해야 하는 개수의 최소값
print(min(target))