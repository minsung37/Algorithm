# https://programmers.co.kr/learn/courses/30/lessons/42883
# 큰 수 만들기
def solution(number, k):
    count, stack, n = 0, [], len(number)
    for i in range(n):
        while count < k and stack and stack[-1] < number[i]:
            stack.pop()
            count = count + 1
        stack.append(number[i])
    return ''.join(stack[:n - k])