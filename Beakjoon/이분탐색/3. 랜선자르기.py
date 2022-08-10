import sys
input = sys.stdin.readline

# 문제조건입력받고 정렬하기
k, n = map(int, input().split())
array = [int(input()) for _ in range(k)]
array.sort()

# 시작값, 끝값
start = 1
end = max(array)


# 렌선 자르기
def cut(array, mid):
    count = 0
    for i in array:
        count = count + (i // mid)
    return count


# 이분탐색
def binary_search(array, target, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        count = cut(array, mid)
        if count < target:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result


# 결과 출력
print(binary_search(array, n, start, end))
