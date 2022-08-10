# https://programmers.co.kr/learn/courses/30/lessons/42885
# 구명보트
def solution(people, limit):
    people.sort()
    answer = 0
    left, right = 0, len(people) - 1
    while left <= right:
        # 가벼운애랑 무거운애 구출
        if people[left] + people[right] <= limit:
            left = left + 1
            right = right - 1
        # 무거운 애만 구출
        else:
            right = right - 1
        answer = answer + 1
    return answer


print(solution([70, 50, 80, 50], 100))
print(solution([70, 50, 80], 100))