import sys
n = int(sys.stdin.readline().rstrip())
x = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())
y = list(map(int, sys.stdin.readline().split()))


def binary(array, target, start, end):
    while end > start:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False


for i in range(m):
    if binary(x, y[i], 0, n - 1):
        print("yes")
    else:
        print("no")