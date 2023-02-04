# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV134DPqAA8CFAYh
# 1206. [S/W 문제해결 기본] 1일차 - View
for t in range(10):
    n = int(input())
    building = list(map(int, input().split()))
    result = 0
    if n == 4:
        print(result)
        continue
    for i in range(2, n - 2):
        one, two = building[i - 2], building[i - 1]
        curr = building[i]
        four, five = building[i + 1], building[i + 2]
        if two >= curr or curr <= four or one >= curr or curr <= five:
            continue
        height = curr - max(one, two, four, five)
        result = result + height
    print("#{} {}".format(t + 1, result))
