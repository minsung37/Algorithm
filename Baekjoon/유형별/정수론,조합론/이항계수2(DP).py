# 파스칼의 삼각형 그리기
n, k = map(int, input().split())

# 초기값 설정
d = [0] * (n + 1)
d[0] = 1
d[1] = [1, 1]

# 예외처리
if n == 1:
    print(1)
# 파스칼의 삼각형 그리기
else:
    for i in range(2, n + 1):
        temp = [1]
        for j in range(int(len(d[i - 1]) - 1)):
            a = (d[i - 1][j] + d[i - 1][j + 1]) % 10007
            temp.append(a)
        temp.append(1)
        d[i] = temp
    print(temp[k])