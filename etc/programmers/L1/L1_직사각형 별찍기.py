# 직사각형 별찍기
# https://school.programmers.co.kr/learn/courses/30/lessons/12969
a, b = map(int, input().strip().split(' '))
for i in range(b):
    for j in range(a):
        print("*", end="")
    print()
