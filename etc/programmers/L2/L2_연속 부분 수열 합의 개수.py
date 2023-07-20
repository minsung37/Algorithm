# 연속 부분 수열 합의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/131701
def solution(elements):
    answer = set()
    temp = elements * 2
    for i in range(1, len(elements) + 1):
        for j in range(len(elements)):
            k = sum(temp[j:j + i])
            answer.add(k)
    return len(answer)


print(solution([7, 9, 1, 1, 4]))
