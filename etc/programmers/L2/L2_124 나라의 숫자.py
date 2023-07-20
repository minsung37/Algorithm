# 124 나라의 숫자
# https://school.programmers.co.kr/learn/courses/30/lessons/12899
def solution(n):
    answer = ""
    while n != 0:
        if n % 3 != 0:
            answer = answer + str(n % 3)
            n = n // 3
        else:
            answer = answer + "4"
            n = n // 3 - 1
    return answer[::-1]


print(solution(4))
print(solution(6))
print(solution(7))
print(solution(12))