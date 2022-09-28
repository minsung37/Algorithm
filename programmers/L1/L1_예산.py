# 예산
# https://school.programmers.co.kr/learn/courses/30/lessons/12982
def solution(d, budget):
    d.sort()
    count = 0
    money = 0
    for d_ in d:
        count = count + 1
        money = money + d_
        if money > budget:
            return count - 1
    return count


print(solution([1, 3, 2, 5, 4], 9))
print(solution([2, 2, 3, 3], 10))