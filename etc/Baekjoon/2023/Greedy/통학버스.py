# 통학버스
# https://www.acmicpc.net/problem/2513
import sys
input = sys.stdin.readline


n, k, s = map(int, input().split())
info_list = [list(map(int, input().split())) for _ in range(n)]
info_list.sort()

left, right = [], []
for info in info_list:
    if info[0] < s:
        left.append(info)
    else:
        right.append(info)
left.reverse()

distance = 0
while left or right:
    l_count, r_count, l_dist, r_dist = k, k, 0, 0
    while left and l_count != 0:
        spot, count = left.pop()
        if l_dist == 0:
            l_dist = s - spot
        if count <= l_count:
            l_count = l_count - count
        else:
            count = count - l_count
            l_count = 0
            left.append([spot, count])
    while right and r_count != 0:
        spot, count = right.pop()
        if r_dist == 0:
            r_dist = spot - s
        if count <= r_count:
            r_count = r_count - count
        else:
            count = count - r_count
            r_count = 0
            right.append([spot, count])
    distance = distance + l_dist + r_dist
print(distance * 2)