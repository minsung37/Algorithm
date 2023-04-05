for _ in range(4):
    coordinate = list(map(int, input().split()))
    x, y, p, q = 0, 1, 2, 3
    box1, box2 = coordinate[:4], coordinate[4:]
    # 안만남
    if box1[p] < box2[x]:
        print('d')
        continue
    if box2[p] < box1[x]:
        print('d')
        continue
    if box1[y] > box2[q]:
        print('d')
        continue
    if box1[q] < box2[y]:
        print('d')
        continue
    # 점
    if box1[x] == box2[p] and box1[y] == box2[q]:
        print("c")
        continue
    if box1[p] == box2[x] and box1[y] == box2[q]:
        print("c")
        continue
    if box1[p] == box2[x] and box1[q] == box2[y]:
        print("c")
        continue
    if box1[x] == box2[p] and box1[q] == box2[y]:
        print("c")
        continue
    # 변
    if box1[q] == box2[y]:
        print("b")
        continue
    if box1[x] == box2[p]:
        print("b")
        continue
    if box1[y] == box2[q]:
        print("b")
        continue
    if box1[p] == box2[x]:
        print("b")
        continue
    # 직사각형
    if box1[x] < box2[p] and box1[y] < box2[q]:
        print("a")
        continue
    if box1[p] > box2[x] and box1[y] < box2[q]:
        print("a")
        continue
    if box1[p] > box2[x] and box1[q] > box2[y]:
        print("a")
        continue
    if box1[x] < box2[p] and box1[q] > box2[y]:
        print("a")
        continue
    print("NOT REACH")