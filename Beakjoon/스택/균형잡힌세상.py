while True:
    a = input()
    if a == ".":
        break
    temp = []
    check = True
    for i in a:
        if i == "(" or i == "[":
            temp.append(i)
        # ")" 전에 "[" 나오거나 비어있으면 안됨
        elif i == ")":
            if not temp or temp[-1] == "[":
                check = False
                break
            # ")" 전에 "(" 가 있으면 짝이 맞으므로 빼줌
            elif temp[-1] == "(":
                temp.pop()
        # "]" 전에 "(" 나오거나 비어있으면 안됨
        elif i == "]":
            if not temp or temp[-1] == "(":
                check = False
                break
            # "]" 전에 "[" 가 있으면 짝이 맞으므로 빼줌
            elif temp[-1] == "[":
                temp.pop()

    # check가 True고 temp가 비어있어야 yes
    # 비어있지 않다는 것은 짝이없는 "("나 "["가 존재한다는 의미
    if check and not temp:
        print("yes")
    else:
        print("no")