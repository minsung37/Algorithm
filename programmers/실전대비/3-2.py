def solution(ingredient):
    stack = []
    burger = 0
    for i in ingredient:
        stack.append(i)
        if i == 1:
            if len(stack) > 3:
                if stack[-2] == 3 and stack[-3] == 2 and stack[-4] == 1:
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    burger = burger + 1
    return burger


print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))