import sys
input = sys.stdin.readline


n, s = map(int, input().split())
array = list(map(int, input().split()))
left, right, result = 0, 0, int(1e9)

if s <= min(array):
    print(1)
    exit(0)
temp = 0
while True:
    if temp >= s:
        result = min(result, right - left)
        temp = temp - array[left]
        left = left + 1
    elif right == n:
        break
    else:
        temp = temp + array[right]
        right = right + 1

if result == int(1e9):
    result = 0
print(result)