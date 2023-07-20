# 점프와 순간 이동
# https://school.programmers.co.kr/learn/courses/30/lessons/12980
def solution(n):
    count = 1
    while n != 1:
        if n % 2 == 1:
            count = count + 1
            n = n // 2
        else:
            n = n // 2
    return count


print(solution(5))
print(solution(6))
print(solution(5000))