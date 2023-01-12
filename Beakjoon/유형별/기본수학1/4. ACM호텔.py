t = int(input())
# 방배정
for i in range(t):
    # 높이, 폭, 몇번째 손님
    h, w, n = map(int, input().split())
    # 순서가 폭의 배수인 경우
    if n % h == 0:
        floor, ho = h, n // h
    else:
        floor, ho = n % h, n // h + 1
    # 정답 출력
    print(floor * 100 + ho)

# 배치 예시
# 9 10 11 12
# 5  6  7  8
# 1  2  3  4