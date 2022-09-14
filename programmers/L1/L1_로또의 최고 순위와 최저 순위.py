# https://school.programmers.co.kr/learn/courses/30/lessons/77484
# 로또의 최고 순위와 최저 순위
def solution(lottos, win_nums):
    low, high = 0, 0
    for lotto in lottos:
        if lotto in win_nums:
            low = low + 1
            win_nums.remove(lotto)

    high = low
    for lotto in lottos:
        if lotto == 0 and len(win_nums) > 0:
            win_nums.pop()
            high = high + 1

    x = 6 if 7 - high >= 6 else 7 - high
    y = 6 if 7 - low >= 6 else 7 - low

    return [x, y]


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))