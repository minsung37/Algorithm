# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14jJh6ACYCFAYD
# 1221. [S/W 문제해결 기본] 5일차 - GNS
dic_to_num = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4,
              "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
dic_to_str = {}
for str_num in dic_to_num:
    dic_to_str[dic_to_num[str_num]] = str_num

n = int(input())
for t in range(n):
    a, b = map(str, input().split())
    b = int(b)
    array = list(map(str, input().split()))
    for idx, num in enumerate(array):
        array[idx] = dic_to_num[num]
    array.sort()
    for idx, num in enumerate(array):
        array[idx] = dic_to_str[num]
    print(a)
    print(*array)