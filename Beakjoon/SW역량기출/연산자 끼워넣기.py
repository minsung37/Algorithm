import sys
input = sys.stdin.readline


n = int(input())
numbers = list(map(int, input().split()))
plus, minus, multi, div = map(int, input().split())
result = []


def backTracking(index, cal, plus, minus, multi, div):
    if index == n - 1:
        result.append(cal)
        return
    if plus > 0:
        backTracking(index + 1, cal + numbers[index + 1], plus - 1, minus, multi, div)
    if minus > 0:
        backTracking(index + 1, cal - numbers[index + 1], plus, minus - 1, multi, div)
    if multi > 0:
        backTracking(index + 1, cal * numbers[index + 1], plus, minus, multi - 1, div)
    if div > 0:
        if cal > 0:
            backTracking(index + 1, cal // numbers[index + 1], plus, minus, multi, div - 1)
        else:
            backTracking(index + 1, -(-cal // numbers[index + 1]), plus, minus, multi, div - 1)


backTracking(0, numbers[0], plus, minus, multi, div)
print(max(result))
print(min(result))