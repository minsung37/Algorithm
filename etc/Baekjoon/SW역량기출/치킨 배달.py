from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
stores, home = [], []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            stores.append([i, j])
        if graph[i][j] == 1:
            home.append([i, j])

result = sys.maxsize
for store in combinations(stores, m):
    temp = 0
    for home_x, home_y in home:
        distance = sys.maxsize
        for store_x, store_y in store:
            distance = min(distance, abs(home_x - store_x) + abs(home_y - store_y))
        temp = temp + distance
    result = min(result, temp)
print(result)