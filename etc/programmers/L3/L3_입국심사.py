# https://school.programmers.co.kr/learn/courses/30/lessons/43238
# 입국심사
def solution(n, times):

    def count_people(target_time):
        count = 0
        for time in times:
            count = count + target_time // time
        return count

    left, right = min(times), max(times) * n
    result = 0

    while left <= right:
        mid = (left + right) // 2
        people = count_people(mid)
        if people >= n:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result


print(solution(6, [7, 10]))