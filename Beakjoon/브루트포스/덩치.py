# 사람수와 가각의 키, 몸무게 입력받기
n = int(input())
weight = []
height = []
for i in range(n):
    a, b = map(int, input().split())
    weight.append(a)
    height.append(b)

# 자기보다 키와 몸무게가 모두 큰사람 체크하기
check = 0
ch = []
for i in range(n):
    x = weight[i]
    y = height[i]
    check = 0
    for j in range(n):
        if x < weight[j] and y < height[j]:
            check = check + 1
    ch.append(check + 1)

# 정답출력
for i in range(n):
    print(ch[i], end=" ")
