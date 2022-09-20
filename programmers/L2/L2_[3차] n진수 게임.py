# [3차] n진수 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/17687
def convertion(number, n):
    array = "0123456789ABCDEF"
    temp = ""
    while number > 0:
        number, r = divmod(number, n)
        temp = temp + array[r]
    return temp[::-1]


# solution에 temp = "" 로 해야함
def convertion2(number, n):
    array = "0123456789ABCDEF"
    q, r = divmod(number, n)
    if q == 0:
        return array[r]
    else:
        return convertion2(q, n) + array[r]


# 진법(n), 미리구할 숫자개수(t), 인원수(m), 내순서(p)
def solution(n, t, m, p):
    answer, temp = "", "0"
    for i in range(m * t):
        temp = temp + str(convertion(i, n))
    for _ in range(t):
        answer = answer + temp[p - 1]
        p = p + m
    return answer


print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))