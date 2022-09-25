# 예상 대진표
# https://school.programmers.co.kr/learn/courses/30/lessons/12985
def solution(n, a, b):
    count = 0
    while a != b:
        a, b = (a + 1) // 2, (b + 1) // 2
        count = count + 1
    return count


print(solution(8, 4, 7))