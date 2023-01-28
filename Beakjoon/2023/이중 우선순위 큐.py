import heapq
import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    dic = defaultdict(int)
    n = int(input())
    heap_min, heap_max = [], []
    count = 0
    for _ in range(n):
        command, number = map(str, input().split())
        number = int(number)
        if command == "I":
            dic[number] = dic[number] + 1
            count = count + 1
            heapq.heappush(heap_min, number)
            heapq.heappush(heap_max, -number)
        elif command == "D":
            if count == 0:
                continue
            count = count - 1
            if number == -1:
                if heap_min:
                    k = heapq.heappop(heap_min)
                    dic[k] = dic[k] - 1
            else:
                if heap_max:
                    k = heapq.heappop(heap_max)
                    dic[-k] = dic[-k] - 1
        while heap_min and dic[heap_min[0]] == 0:
            heapq.heappop(heap_min)
        while heap_max and dic[-heap_max[0]] == 0:
            heapq.heappop(heap_max)
    if count == 0:
        print("EMPTY")
    else:
        result = []
        for i in dic:
            if dic[i] > 0:
                result.append(i)
        print(max(result), min(result))