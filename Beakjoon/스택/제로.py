from collections import deque

n = int(input())
array = deque()

for i in range(n):
    a = int(input())
    if a == 0:
        array.pop()
    else:
        array.append(a)

print(sum(array))