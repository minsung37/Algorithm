def solution(order):
    truck, belt = [], [0]
    order.reverse()
    for i in range(len(order)):
        if i + 1 == order[-1]:
            truck.append(order.pop())
        else:
            belt.append(i + 1)
        while belt[-1] == order[-1]:
            belt.pop()
            truck.append(order.pop())
            if len(order) == 0:
                break
    return len(truck)


print(solution([4, 3, 1, 2, 5]))
print(solution([5, 4, 3, 2, 1]))