import sys
from collections import Counter

n = int(sys.stdin.readline())

array = []
for i in range(n):
    array.append(int(sys.stdin.readline()))
array.sort()

# 평균
avg = round(sum(array) / n, 0)
# 중앙값
mid = array[n // 2]
# 범위
size = array[n - 1] - array[0]
# 최빈값
cnt = Counter(array).most_common(2)
if len(array) > 1:
    #
    if cnt[0][1] == cnt[1][1]:
        res = cnt[1][0]
    else:
        res = cnt[0][0]
else:
    res = cnt[0][0]


# 산술평균
print(int(f'{avg:.0f}'))
# 중앙값
print(mid)
# 최빈값
print(res)
# 범위
print(size)
