# 혼자 놀기의 달인
# https://school.programmers.co.kr/learn/courses/30/lessons/131130
def solution(cards):
    visited = [False] * len(cards)
    stack, result = [], []

    for i in range(len(cards)):
        count = 0
        if not visited[i]:
            visited[i] = True
            stack.append(cards[i])
            while stack:
                count = count + 1
                k = stack.pop()
                if not visited[k - 1]:
                    stack.append(cards[k - 1])
                    visited[k - 1] = True
        if count > 0:
            result.append(count)

    result.sort()
    if len(result) == 1:
        return 0
    return result[-1] * result[-2]


print(solution([8, 6, 3, 7, 2, 5, 1, 4]))
