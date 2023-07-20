t = int(input())

for _ in range(t):
    # 층수, 호수 입력받기
    floor = int(input())
    num = int(input())
    # 0층
    f = [x for x in range(1, num + 1)]
    for _ in range(floor):
        for i in range(1, num):
            f[i] = f[i] + f[i - 1]
    print(f[-1])