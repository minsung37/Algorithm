# https://programmers.co.kr/learn/courses/30/lessons/42587
# 프린터
def solution(priorities, location):
    printer, order = [], 0
    for index, value in enumerate(priorities):
        if index == location:
            printer.append([value, 1])
        else:
            printer.append([value, 0])

    while priorities:
        x, y = printer.pop(0), priorities.pop(0)
        document, check = x[0], x[1]
        order = order + 1
        if not priorities:
            return order
        if max(priorities) > document:
            printer.append([document, check])
            priorities.append(y)
            order = order - 1
            continue
        if check:
            return order


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))