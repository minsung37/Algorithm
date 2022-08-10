from collections import deque
import sys
n = int(sys.stdin.readline())

deque = deque()
for i in range(n):
    a = sys.stdin.readline().split()

    # push_front X: 정수 X를 덱의 앞에 넣는다.
    if a[0] == "push_front":
        deque.appendleft(a[1])

    # push_back X: 정수 X를 덱의 뒤에 넣는다.
    elif a[0] == "push_back":
        deque.append(a[1])

    # pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif a[0] == "pop_front":
        if len(deque) == 0:
            print(-1)
        else:
            b = deque.popleft()
            print(b)

    # pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif a[0] == "pop_back":
        if len(deque) == 0:
            print(-1)
        else:
            b = deque.pop()
            print(b)

    # size: 덱에 들어있는 정수의 개수를 출력한다.
    elif a[0] == "size":
        print(len(deque))

    # empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
    elif a[0] == "empty":
        if len(deque) == 0:
            print(1)
        else:
            print(0)

    # front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif a[0] == "front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])

    # back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif a[0] == "back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])