while True:
    # 수를 문자열로 받는다
    n = input()
    if n == "0":
        break
    else:
        b = len(n)
        # 입력받은 수를 뒤집어서 배열에 넣는다
        c = []
        for i in range(b):
            a = n[b - i - 1]
            c.append(a)
        # 입력받은 수 그대로 배열에 넣는다.
        d = []
        for i in range(b):
            e = n[i]
            d.append(e)
        # 입력받은 수와 뒤집은 수를 비교한다.
        if c == d:
            print("yes")
        else:
            print("no")

