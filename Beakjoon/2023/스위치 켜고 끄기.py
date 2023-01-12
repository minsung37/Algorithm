def switch(k):
    if light[k] == 1:
        light[k] = 0
    else:
        light[k] = 1


n = int(input())
light = [3] + list(map(int, input().split()))
t = int(input())
for _ in range(t):
    gender, spot = map(int, input().split())
    count = 1
    if gender == 1:
        while spot * count <= n:
            switch(spot * count)
            count = count + 1
    else:
        distance = 1
        switch(spot)
        while spot - distance > 0 and spot + distance <= n:
            if light[spot - distance] == light[spot + distance]:
                switch(spot - distance)
                switch(spot + distance)
                distance = distance + 1
            else:
                break
for i in range(1, len(light)):
    print(light[i], end=" ")
    if i % 20 == 0:
        print()