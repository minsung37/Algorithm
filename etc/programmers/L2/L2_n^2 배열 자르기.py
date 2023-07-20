# n^2 배열 자르기
# https://school.programmers.co.kr/learn/courses/30/lessons/87390
def solution(n, left, right):
    result = []

    for i in range(left, right + 1):
        quotient, remainder = i // n, i % n
        if quotient < remainder:
            quotient, remainder = remainder, quotient
        result.append(quotient + 1)

    return result


print(solution(3, 2, 5))
print(solution(4, 7, 14))
