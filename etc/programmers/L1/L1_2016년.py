# https://school.programmers.co.kr/learn/courses/30/lessons/12901
# 2016년
def solution(a, b):
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    long = [1, 3, 5, 7, 8, 10, 12]
    short = [4, 6, 9, 11]
    count = 0
    a = a - 1
    while a != 0:
        if a in long:
            count = count + 31
        if a in short:
            count = count + 30
        if a == 2:
            count = count + 29
        a = a - 1
    return day[(count + b) % 7 - 1]


print(solution(5, 24))