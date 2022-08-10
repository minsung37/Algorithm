n = int(input())
# 더하기 사이클
z = n
count = 0
while True:
    # 한자리수 인경우
    if z < 10:
        z = int(str(z) + str(z))
    else:
        # z = 26
        z = str(z)
        # 2 + 6 = 8(x)
        x = int(z[0]) + int(z[1])
        x = str(x)
        # 68
        z = int(z[-1] + x[-1])
    count = count + 1
    if z == n:
        print(count)
        break