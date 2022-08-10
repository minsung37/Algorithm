# https://leetcode.com/problems/trapping-rain-water/
# 136ms 15.7MB - 투포인터 풀이
def trap(height: list[int]) -> int:

    if not height:
        return 0
    volume, left, right = 0, 0, len(height) - 1
    left_max, right_max = height[0], height[-1]

    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)
        if left_max <= right_max:
            volume = volume + left_max - height[left]
            left = left + 1
        else:
            volume = volume + right_max - height[right]
            right = right - 1
    return volume



