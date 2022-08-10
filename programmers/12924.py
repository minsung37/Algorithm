# https://programmers.co.kr/learn/courses/30/lessons/12924
# 숫자의 표현
def solution(n):
    # 예외처리
    if n == 1 or n == 2:
        return 1
    count = 0
    # 홀수인경우 2가지로 가능함
    if n % 2 == 1:
        count = count + 1
    # 홀수로 나눈경우에만 가능함
    for i in range(3, n // 2 + 1, 2):
        if n % i == 0:
            count = count + 1
    # 자기자신 + 1
    return count + 1


print(solution(15))
print(solution(1))
print(solution(2))
