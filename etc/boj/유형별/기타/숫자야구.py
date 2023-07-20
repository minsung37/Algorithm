array = [True] * 1000
count = 0
for i in range(123, 988):
    str_i = str(i)
    # 중복숫자
    if len(set(str_i)) < 3:
        array[i] = False
    # 0포함 숫자
    if "0" in str_i:
        array[i] = False

# 숫자야구
n = int(input())
for _ in range(n):
    num, s, b = map(int, input().split())
    check_num = str(num)
    for k in range(123, 988):
        strike = 0
        ball = 0
        target_num = str(k)
        for x in range(3):
            for y in range(3):
                if check_num[x] == target_num[y]:
                    if x == y:
                        strike = strike + 1
                    else:
                        ball = ball + 1
        if strike != s or ball != b:
            array[k] = False

for i in range(123, 988):
    if array[i]:
        count = count + 1
print(count)