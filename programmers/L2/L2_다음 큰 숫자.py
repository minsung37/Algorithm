# 다음 큰 숫자
# https://school.programmers.co.kr/learn/courses/30/lessons/12911
def solution(n):
    first_bin = str(bin(n)).count("1")
    while True:
        n = n + 1
        second_bin = str(bin(n)).count("1")
        if first_bin == second_bin:
            break
    return n


print(solution(78))
print(solution(15))