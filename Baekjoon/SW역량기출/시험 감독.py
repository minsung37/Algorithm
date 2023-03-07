import math
import sys
input = sys.stdin.readline


n = int(input())
rooms = list(map(int, input().split()))
b, c = map(int, input().split())
count = 0
for room in rooms:
    room = room - b
    count = count + 1
    if room > 0:
        count = count + math.ceil(room / c)
print(count)