import sys
input = sys.stdin.readline


n = int(input())
solutions = list(map(int, input().split()))


left, right = 0, n - 1
value = abs(solutions[left] + solutions[right])
res_left, res_right = solutions[left], solutions[right]
while left < right:
    temp_value = solutions[left] + solutions[right]
    if abs(temp_value) < value:
        value = abs(temp_value)
        res_left, res_right = solutions[left], solutions[right]
    if temp_value > 0:
        right = right - 1
    else:
        left = left + 1
print(res_left, res_right)
