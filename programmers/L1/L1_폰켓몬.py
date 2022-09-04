# https://school.programmers.co.kr/learn/courses/30/lessons/1845
# 폰켓몬
def solution(nums):
    nums_ = list(set(nums))
    answer = len(nums_)
    if answer > len(nums) // 2:
        answer = len(nums) // 2
    return answer