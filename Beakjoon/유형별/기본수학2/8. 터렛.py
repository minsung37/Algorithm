import math
import sys
n = int(input())

for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    ro = r1 + r2
    ri = abs(r1 - r2)
    s = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    # 두원 겹치는 경우
    if s == 0 and r1 == r2:
        print(-1)
    # 접점1
    elif ro == s or ri == s:
        print(1)
    # 접점2
    elif ri < s < ro:
        print(2)
    # 그외
    else:
        print(0)

# x1, y1, r1, x2, y2, r2가 주어진다. x1, y1, x2, y
# r1 + r2 < d 이면 두 원은 서로의 외부에 위치한다.
# r1 + r2 = d 이면 두 원은 외접한다.
# |r1 - r2| < d < r1 + r2 이면 두 원은 서로 다른 두 점에서 만난다.
# |r1 - r2| = d 이면 한 원이 다른 원에 내접한다.
# |r1 - r2| > d, r1 ≠ r2 이면 한 원이 다른 원의 내부에 있다.