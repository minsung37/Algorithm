import heapq
import sys
input = sys.stdin.readline

# 입력받기
n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

# 절대값,음수,양수
heap_abs = []
heap_negative = []
heap_positive = []
# 리스트를 힙으로
heapq.heapify(heap_abs)
heapq.heapify(heap_negative)
heapq.heapify(heap_positive)
for i in array:
    # 힙이 비었을경우
    if i == 0 and len(heap_abs) == 0:
        print(0)
    elif i == 0:
        # 음수힙안에 숫자있는경우
        if len(heap_negative) != 0:
            # 절대값힙에서 꺼낸값이 음수힙에 있을때
            if heapq.heappop(heap_abs) == abs(heap_negative[0]):
                print(-heapq.heappop(heap_negative))
            # 절대값힙에서 꺼낸값이 음수힙에 없을때 양수힙에서 꺼냄
            else:
                print(heapq.heappop(heap_positive))
        # 음수힙이 없으면 양수힙에서 출력
        else:
            print(heapq.heappop(heap_positive))
            heapq.heappop(heap_abs)
    else:
        # 힙에 원소 넣기
        heapq.heappush(heap_abs,abs(i))
        if i < 0:
            heapq.heappush(heap_negative, -i)
        else:
            heapq.heappush(heap_positive, i)