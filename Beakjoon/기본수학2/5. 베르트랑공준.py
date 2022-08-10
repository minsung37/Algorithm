import sys
import math

limit = 123456
# 배열의 크기를 선언하고 값을 1로 초기화
eratos = [1] * (2 * limit + 1)
# 0, 1 제외
eratos[0] = 0
eratos[1] = 0

# 2부터 배열의길이의 제곱근 값까지 탐색
for i in range(2, int(math.sqrt(len(eratos)))):
    # 2를 제외한 2의 배수제거 배열의 끝까지 3을 제외한 3의 배수제거...
    for j in range(i + i, len(eratos), i):
        eratos[j] = 0

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    else:
        # n+1 부터 2n까지의 소수개수출력
        print(sum(eratos[n + 1:(2 * n) + 1]))

