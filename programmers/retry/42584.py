# https://programmers.co.kr/learn/courses/30/lessons/42584
# 주식가격
def solution(prices):
    answer = [len(prices) - i - 1 for i in range(len(prices))]
    stack = [0]
    for i in range(1, len(prices)):
        while stack:
            index = stack[-1]
            if prices[index] > prices[i]:
                answer[index] = i - index
                stack.pop()
            else:
                break
        stack.append(i)
    return answer


print(solution([1, 2, 3, 2, 3]))