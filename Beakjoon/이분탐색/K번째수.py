n = int(input())
k = int(input())
start = 1
end = n ** 2

# 이분탐색
while start <= end:
    mid = (start + end) // 2
    check = 0
    # 임의의수 mid는 check번째수임
    for i in range(1, n + 1):
        # n개를 넘어갈 수 없음
        temp = min(mid // i, n)
        check = check + temp
    # 뒤를 땡기는경우
    if check >= k:
        answer = mid
        end = mid - 1
    # 앞을 땡기는경우
    else:
        start = mid + 1

# 정답출력
print(answer)