# 정수 N을 입력받기
n = int(input())
# 모든 식량 정보 입력받기
array = list(map(int, input().split()))
# 위치
k = 0
# 값
res = 0
while True:
    # 연속된 3개 선택해서 끝값과 중앙값 비교
    if array[k] + array[k + 2] < array[k + 1]:
        res = res + array[k + 1]
        # 다음 선택위치
        k = k + 3
    else:
        res = res + array[k] + array[k + 2]
        # 다음 선택위치
        k = k + 4
    # 예외처리
    if k == n - 3:
        res = res + array[n - 3] + array[n - 1]
        break
    if k == n - 2:
        res = res + array[n - 2]
        break
    if k == n - 1:
        res = res + array[n - 1]
        break
    if k == n:
        break

print(res)