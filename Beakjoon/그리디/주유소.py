import sys
n = int(input())
roads = list(map(int, sys.stdin.readline().split()))
costs = list(map(int, sys.stdin.readline().split()))

result = 0
c = costs[0]

for i in range(n-1):
    if costs[i] < c:
        c = costs[i]
    result = result + c * roads[i]

print(result)