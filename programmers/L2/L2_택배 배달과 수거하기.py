# 택배 배달과 수거하기
# https://school.programmers.co.kr/learn/courses/30/lessons/150369
def solution(cap, n, deliveries, pickups):
    distance = 0
    while deliveries or pickups:
        d_count, p_count, d_dist, p_dist = cap, cap, 0, 0
        while deliveries and d_count != 0:
            k = deliveries.pop()
            if k == 0:
                continue
            if d_dist == 0:
                d_dist = len(deliveries) + 1
            if k <= d_count:
                d_count = d_count - k
            else:
                k = k - d_count
                d_count = 0
                deliveries.append(k)
        while pickups and p_count != 0:
            k = pickups.pop()
            if k == 0:
                continue
            if p_dist == 0:
                p_dist = len(pickups) + 1
            if k <= p_count:
                p_count = p_count - k
            else:
                k = k - p_count
                p_count = 0
                pickups.append(k)
        distance = distance + max(d_dist, p_dist)
    return distance * 2


print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
