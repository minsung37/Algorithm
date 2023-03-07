while True:
    n, m = map(int, input().split())
    # 마지막 입력 0 0
    if n == 0 and m == 0:
        break
    # n은 m의 약수
    if n // m == 0 and m % n == 0:
        print("factor")
    # n은 m의 배수
    elif n // m != 0 and n % m == 0:
        print("multiple")
    else:
        print("neither")