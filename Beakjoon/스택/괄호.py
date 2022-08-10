# testcase수
n = int(input())

for i in range(n):
    count = 0
    a = input()
    for j in a:
        if j == "(":
            count = count + 1
        elif j == ")":
            count = count - 1
        # ")"가 먼저 "("와 쌍을 이루기전에 먼저 나옴 => "()"를 만족시키지 못함
        if count < 0:
            break
    # "(", ")" 각각 수가 같아야함
    if count == 0:
        print("YES")
    else:
        print("NO")