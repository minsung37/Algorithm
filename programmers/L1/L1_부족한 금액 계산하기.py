# 부족한 금액 계산하기
# https://school.programmers.co.kr/learn/courses/30/lessons/82612
def solution(price, money, count):
    total = 0
    for i in range(1, count + 1):
        total = total + i
    if money - price * total < 0:
        return price * total - money
    return 0


print(solution(3, 20, 4))