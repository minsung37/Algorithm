# https://programmers.co.kr/learn/courses/30/lessons/42578
# 위장
import collections


def solution(clothes):
    style = collections.defaultdict(list)
    for cloth, kind in clothes:
        style[kind].append(cloth)

    count = 1
    for kind in style:
        count = count * (len(style[kind]) + 1)
    # 아무것도 안입은 경우 제외
    return count - 1


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))