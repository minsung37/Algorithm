import sys
import math
input = sys.stdin.readline


# 배열의 크기를 선언하고 값을 1로 초기화
limit = 10001
eratos = [True for i in range(limit + 1)]
# 0, 1 제외
eratos[0] = False
eratos[1] = False

# 2부터 배열의길이의 제곱근 값까지 탐색
for i in range(2, int(math.sqrt(len(eratos)) + 1)):
    if eratos[i]:
        # 2를 제외한 2의 배수제거 배열의 끝까지 3을 제외한 3의 배수제거...
        for j in range(i + i, len(eratos), i):
            eratos[j] = False

# 정답출력
n = int(input())
for i in range(n):
    a = int(input())
    x = int(a / 2)
    y = a - x
    for j in range(int(a/2)):
        # 두수 모두 소수이면 출력
        if eratos[y] and eratos[x]:
            print(y, x)
            break
        # 아닐경우 1씩 증, 감
        else:
            x = x + 1
            y = y - 1