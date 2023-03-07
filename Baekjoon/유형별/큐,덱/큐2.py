from collections import deque
import sys

n = int(sys.stdin.readline())
queue = deque()

for i in range(n):
    a = sys.stdin.readline().split()

    # push X: 정수 X를 큐에 넣는 연산이다.
    if a[0] == "push":
        queue.append(a[1])

    # pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif a[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    # size: 큐에 들어있는 정수의 개수를 출력한다.
    elif a[0] == "size":
        print(len(queue))

    # empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
    elif a[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    # front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif a[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    # back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif a[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])