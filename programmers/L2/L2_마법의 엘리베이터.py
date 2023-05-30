# 마법의 엘리베이터
# https://school.programmers.co.kr/learn/courses/30/lessons/148653


def solution(storey):
    result = 0
    while storey:
        curr = storey % 10
        next = (storey // 10) % 10
        if 0 <= curr < 5:
            result = result + curr
        elif curr == 5:
            if next >= 5:
                storey = storey + curr
            result = result + curr
        else:
            result = result + (10 - curr)
            storey = storey + 10
        storey = storey // 10
    return result


print(solution(16))
print(solution(2554))