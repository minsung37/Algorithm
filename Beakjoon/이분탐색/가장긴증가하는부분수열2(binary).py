# 이진탐색구현
def binary(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if dp[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start


# 문제 정보 입력받기
n = int(input())
array = list(map(int, input().split()))
# LIS
dp = [0]
for i in array:
    if dp[-1] < i:
        dp.append(i)
    else:
        dp[binary(0, len(dp) - 1, i)] = i
# 정답 출력
print(len(dp) - 1)