# 연속된 부분 수열의 합
# https://school.programmers.co.kr/learn/courses/30/lessons/178870
def solution(sequence, k):
    sum_value = 0
    left, right = 0, 0
    result = [0, len(sequence)]
    for index, value in enumerate(sequence):
        sum_value = sum_value + value
        right = index
        if sum_value == k:
            if result[1] - result[0] > right - left:
                result = [left, right]
        while sum_value > k:
            sum_value = sum_value - sequence[left]
            left = left + 1
            if sum_value == k:
                if result[1] - result[0] > right - left:
                    result = [left, right]
    return result


print(solution([1, 2, 3, 4, 5], 7))
print(solution([1, 1, 1, 2, 3, 4, 5], 5))
print(solution([2, 2, 2, 2, 2], 6))