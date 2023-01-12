from collections import deque


n = int(input())
check = [0, 0, 0, 0, 0]
queue = deque()

for i in range(6):
    idx, length = map(int, input().split())
    check[idx] = check[idx] + 1
    queue.append([idx, length])

while True:
    if check[queue[0][0]] == 1 and check[queue[1][0]] == 1:
        break
    queue.append(queue.popleft())


print((queue[0][1] * queue[1][1] - queue[4][1] * queue[3][1]) * n)