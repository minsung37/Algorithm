import sys

n = int(sys.stdin.readline())
set0 = set()

for i in range(n):
    a = list(sys.stdin.readline().split())
    if len(a) > 1:
        a[1] = int(a[1])
        x = a[1]

    # add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
    if a[0] == "add":
        set0.add(x)

    # remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
    elif a[0] == "remove":
        try:
            set0.remove(x)
        except:
            continue

    # check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
    elif a[0] == "check":
        if x in set0:
            print(1)
        else:
            print(0)

    # toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
    elif a[0] == "toggle":
        if x in set0:
            set0.remove(x)
        else:
            set0.add(x)

    # all: S를 {1, 2, ..., 20} 으로 바꾼다.
    elif a[0] == "all":
        set0 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

    # empty: S를 공집합으로 바꾼다.
    elif a[0] == "empty":
        set0 = set()
