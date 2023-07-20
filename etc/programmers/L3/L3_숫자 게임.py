# 숫자 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/12987
def solution(A, B):
    A.sort(reverse=True)
    B.sort()
    for num in A:
        if num < B[-1]:
            B.pop()
    return len(A) - len(B)


print(solution([5, 1, 3, 7], [2, 2, 6, 8]))
print(solution([2, 2, 2, 2], [1, 1, 1, 1]))
