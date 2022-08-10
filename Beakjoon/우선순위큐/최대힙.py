import heapq
import sys
input = sys.stdin.readline

n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

heap = []
# 리스트를 힙으로
heapq.heapify(heap)
for i in array:
    if i == 0 and len(heap) == 0:
        print(0)
    elif i == 0:
        # 힙의 원소 추출
        print(abs(heapq.heappop(heap)))
    else:
        # 힙에 원소 넣기
        heapq.heappush(heap, -i)