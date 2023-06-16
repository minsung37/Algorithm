# 우박수열 정적분
# https://school.programmers.co.kr/learn/courses/30/lessons/134239
def solution(k, ranges):
    y = [k]
    while k > 1:
        if k % 2 == 0:
            k = k // 2
        else:
            k = k * 3 + 1
        y.append(k)

    result = []
    for x1, x2 in ranges:
        x2 = len(y) - 1 + x2
        if x1 == x2:
            result.append(0)
        elif x1 > x2:
            result.append(-1)
        else:
            size = 0
            for x in range(x1, x2):
                if x == len(y) - 1:
                    break
                size = size + (y[x] + y[x + 1]) / 2
            result.append(size)
    return result


print(solution(5, [[0, 0], [0, -1], [2, -3], [3, -3]]))