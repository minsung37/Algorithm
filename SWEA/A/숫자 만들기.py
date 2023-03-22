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


T = int(input())
for t in range(T):
    n = int(input())
    plus, minus, multi, div = map(int, input().split())
    numbers = list(map(int, input().split()))
    result = []
    backTracking(0, numbers[0], plus, minus, multi, div)
    print("#%d %d" % (t + 1, max(result) - min(result)))