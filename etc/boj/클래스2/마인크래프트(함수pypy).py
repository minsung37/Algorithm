import sys
input = sys.stdin.readline


def check(target, brick):
    global n, m, mintime
    time = 0
    for i in range(n):
        for j in range(m):
            if mintime < time:
                return -1
            if target < array[i][j]:
                time = time + (array[i][j] - target) * 2
                brick = brick + (array[i][j] - target)
            else:
                time = time - (array[i][j] - target)
                brick = brick + (array[i][j] - target)
    if brick < 0:
        return -1
    return time


n, m, b = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

mintime, height = 1000000000, 0
for target in range(257):
    time = check(target, b)
    if 0 <= time <= mintime:
        mintime = time
        height = target

print(mintime, height)