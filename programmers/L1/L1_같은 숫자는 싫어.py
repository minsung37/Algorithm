# https://school.programmers.co.kr/learn/courses/30/lessons/12906
# 같은 숫자는 싫어
def solution(arr):
    stack = [-1]
    for i in arr:
        if i != stack[-1]:
            stack.append(i)
    return stack[1:]


print(solution([1, 1, 3, 3, 0, 1, 1]))