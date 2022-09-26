# 삼각 달팽이
# https://school.programmers.co.kr/learn/challenges?order=acceptance_asc&page=2&levels=2
def solution(n):
    snail = [[0] * n for _ in range(n)]
    x, y = -1, 0
    number, result = 1, []
    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0:
                x = x + 1
            elif i % 3 == 1:
                y = y + 1
            elif i % 3 == 2:
                x = x - 1
                y = y - 1
            snail[x][y] = number
            number = number + 1
    for nums in snail:
        for num in nums:
            if num != 0:
                result.append(num)
    return result


print(solution(4))
print(solution(5))
print(solution(6))