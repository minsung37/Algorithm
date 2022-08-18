# https://school.programmers.co.kr/learn/courses/30/lessons/42583
# 다리를 지나는 트럭
from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_weights.reverse()
    bridge = deque([0] * bridge_length)
    count, bridge_weight = 0, 0
    while bridge:
        count = count + 1
        bridge_weight = bridge_weight - bridge.popleft()
        if truck_weights:
            if (bridge_weight + truck_weights[-1]) <= weight:
                bridge_weight += truck_weights[-1]
                bridge.append(truck_weights.pop())
            else:
                bridge.append(0)
    return count


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))