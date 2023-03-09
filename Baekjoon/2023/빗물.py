import sys
input = sys.stdin.readline

h, w = map(int, input().split())
height = list(map(int, input().split()))

# 좌우 투포인터 설정
left, right = 0, len(height) - 1
left_max, right_max = height[0], height[-1]

# 빗물트래킹 => 좌, 우 높은 것중에 작은것을 기준으로 빗물 담기
raindrop = 0
while left < right:
    left_max = max(left_max, height[left])
    right_max = max(right_max, height[right])
    if left_max < right_max:
        raindrop = raindrop + (left_max - height[left])
        left = left + 1
    else:
        raindrop = raindrop + (right_max - height[right])
        right = right - 1
print(raindrop)