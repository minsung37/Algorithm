import math

# n! 구해서 문자로 치환
n = int(input())
num = math.factorial(n)
target = str(num)

# 0의 개수 카운트
count = 1
i = 1

# 마지막수가 0이 아닌경우
if target[len(target) - 1] != "0":
    print(0)

# 마지막수 0인경우
else:
    while True:
        # 0이 아닐때까지 반복
        if target[len(target) - 1 - i] == "0":
            count = count + 1
            i = i + 1
        else:
            break
    # 결과출력
    print(count)