import math
# 숫자쌍 개수
t = int(input())

# 최소공배수(Least Common Multiple)
for i in range(t):
    n, m = map(int, input().split())
    lcm = math.lcm(n, m)
    print(lcm)
# 시간초과
# for i in range(t):
#     n, m = map(int, input().split())
#     k = 1
#     while True:
#         lcm = m * k
#         if lcm % n == 0:
#             break
#         else:
#             k = k + 1
#     print(lcm)