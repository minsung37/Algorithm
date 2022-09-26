# 최솟값 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12941
def solution(A, B):
    A.sort()
    B.sort(reverse=True)
    answer = 0
    for i in range(len(A)):
        answer = answer + A[i] * B[i]
    return answer


print(solution([1, 4, 2], [5, 4, 4]))
print(solution([1, 2], [3, 4]))