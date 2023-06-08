def print_nums():
    num1 = 0
    num2 = 0

    def change_num():
        nonlocal num1
        global num2
        num1 = 100
        num2 = 100
        print(num1, "num1")
        print(num2, "num2")
    change_num()
    print(num1, "num1")
    print(num2, "num2")


print_nums()