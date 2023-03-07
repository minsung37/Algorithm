# 반복횟수 입력받기
n = int(input())

# d 초기화
d = [0] * 101
d[1] = 1
d[2] = 1
d[3] = 1
d[4] = 2

# 점화식대로 d에 넣기
for i in range(5, 101):
    d[i] = d[i - 1] + d[i - 5]

# 결과출력
for i in range(n):
    b = int(input())
    print(d[b])