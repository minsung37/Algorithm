# 문자열 입력받기
s = input()

# 1을 기준 으로 나누기
a = s.split("1")
count_a = 0
# 문자열의 길이가 0보다 큰것 카운트
for i in a:
    if len(i) > 0:
        count_a = count_a + 1

# 0을 기준으로 나누기
b = s.split("0")
count_b = 0
# 문자열의 길이가 0보다 큰것 카운트
for i in b:
    if len(i) > 0:
        count_b = count_b + 1

# 정답출력
print(min(count_a, count_b))