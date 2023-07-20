# 징검다리 건너기
# https://school.programmers.co.kr/learn/courses/30/lessons/64062
def solution(stones, k):
    left, right = 1, 200000000
    while left <= right:
        mid = (left + right) // 2
        count = 0
        up = True
        for stone in stones:
            if stone - mid <= 0:
                count = count + 1
                if count >= k:
                    up = False
                    break
            else:
                count = 0
        if up:
            left = mid + 1
        else:
            right = mid - 1
    return left


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))