# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LsaaqDzYDFAXc
# 1860. 진기의 최고급 붕어빵
T = int(input())
for t in range(T):
    n, m, k = map(int, input().split())
    time_list = list(map(int, input().split()))
    time_list.sort()
    make_list = [0] * n
    flag = True
    for index, time in enumerate(time_list):
        make_list[index] = (time // m) * k
    for index, value in enumerate(time_list):
        if make_list[index] - index < 1:
            flag = False
            break
    if flag:
        print('#{} {}'.format(t + 1, "Possible"))
    else:
        print('#{} {}'.format(t + 1, "Impossible"))