from collections import deque
import sys
input = sys.stdin.readline

wheels = []
for _ in range(4):
    temp = deque()
    wheel = input().rstrip()
    for i in wheel:
        temp.append(i)
    wheels.append(temp)

n = int(input())
for _ in range(n):
    order, direction = map(int, input().split())
    dic = {0: False, 1: False, 2: False, 3: False, 4: False}
    if wheels[0][2] != wheels[1][6]:
        dic[1] = True
    if wheels[1][2] != wheels[2][6]:
        dic[2] = True
    if wheels[2][2] != wheels[3][6]:
        dic[3] = True
    order = order - 1
    left, right = -direction, -direction
    wheels[order].rotate(direction)
    # 왼쪽 톱니
    if dic[order]:
        for i in range(order - 1, -1, -1):
            wheels[i].rotate(left)
            left = -left
            if i == 0 or not dic[i]:
                break
    # 오른쪽 톱니
    if dic[order + 1]:
        for i in range(order + 1, 4):
            wheels[i].rotate(right)
            right = -right
            if i == 3 or not dic[i + 1]:
                break

result = 0
for index, wheel in enumerate(wheels):
    result = result + (2 ** index) * int(wheel[0])
print(result)