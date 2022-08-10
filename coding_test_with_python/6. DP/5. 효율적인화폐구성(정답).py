# n, m 입력받기
n, m = map(int, input().split())

# 화폐 정보 입력받기
array = []
for i in range(n):
    array.append(int(input()))

# 한번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍 진행(바텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        # (i - k)원을 만드는 방법이 존재하지 않는경우
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001:
    print(-1)
else:
    print(d[m])