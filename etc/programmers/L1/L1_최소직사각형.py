# https://school.programmers.co.kr/learn/courses/30/lessons/86491
# 최소직사각형
def solution(sizes):
    width, height = [], []
    # 큰거를 가로 작은거를 세로
    for x, y in sizes:
        if x >= y:
            width.append(x)
            height.append(y)
        else:
            height.append(x)
            width.append(y)
    return max(width) * max(height)


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))