# 점 찍기
# https://school.programmers.co.kr/learn/courses/30/lessons/140107
def solution(k, d):
    count = 0
    for i in range(0, d + 1, k):
        temp = int((d ** 2 - i ** 2) ** 0.5)
        count = count + (temp // k) + 1
    return count


print(solution(2, 4))
print(solution(1, 5))