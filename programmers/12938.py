# https://programmers.co.kr/learn/courses/30/lessons/12938
# 최고의 집합
def solution(n, s):
    div = s // n
    answer = [div] * n
    if div == 0:
        return [-1]
    if sum(answer) == s:
        return answer
    else:
        rest = s - sum(answer)
        for i in range(rest):
            answer[i] = answer[i] + 1
    return sorted(answer)


print(solution(2, 9))