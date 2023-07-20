# https://programmers.co.kr/learn/courses/30/lessons/42862
# 체육복
def solution(n, lost, reserve):
    reserve_ = set(reserve) - set(lost)
    lost_ = set(lost) - set(reserve)

    for i in reserve_:
        front = i - 1
        back = i + 1
        if front in lost_:
            lost_.remove(front)
        elif back in lost_:
            lost_.remove(back)
    return n - len(lost_)