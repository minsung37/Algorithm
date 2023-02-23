import sys
input = sys.stdin.readline
n = int(input())

# 조커 제외 카드 담고, 조커 카운트, 가진카드 체크
number_list = list(map(int, input().split()))
have_card = [False] * (max(number_list) + 1)
zero = 0
for i in range(n):
    num = number_list[i]
    if num == 0:
        zero = zero + 1
    else:
        have_card[num] = True
if n == zero:
    print(n)
    exit(0)
straight = 0
for num in range(1, len(have_card) - 1):
    temp_zero_count = zero
    temp_straight = 1
    flag = False
    while num < len(have_card) - 1:
        if not flag:
            if not have_card[num]:
                if temp_zero_count == 0:
                    break
                temp_zero_count = temp_zero_count - 1
        if not have_card[num + 1]:
            if temp_zero_count <= 0:
                break
            temp_zero_count = temp_zero_count - 1
        temp_straight = temp_straight + 1
        num = num + 1
        flag = True
    straight = max(straight, temp_straight + temp_zero_count)
print(straight)