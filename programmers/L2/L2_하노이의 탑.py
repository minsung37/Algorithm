# 하노이의 탑
# https://school.programmers.co.kr/learn/courses/30/lessons/12946
def solution(n):

    def hanoi(num, start, target):
        if num > 1:
            hanoi(num - 1, start, 6 - start - target)
        answer.append([start, target])
        if num > 1:
            hanoi(num - 1, 6 - start - target, target)

    answer = []
    hanoi(n, 1, 3)
    return answer


print(solution(2))