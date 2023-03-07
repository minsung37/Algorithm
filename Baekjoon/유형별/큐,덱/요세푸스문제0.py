# n, k 입력받기
n, k = map(int, input().split())

# 1 ~ n 까지 담기
array = []
for i in range(1, n + 1):
    array.append(i)

# 요세푸스 수열 구하기
yose = []
d = k - 1
for i in range(n):
    d = d % n
    b = array.pop(d)
    yose.append(b)
    d = d + (k - 1)
    n = n - 1

# 정답 출력
print("<", end='')
for i in range(len(yose) - 1):
    print("%d, " % yose[i], end='')
print(yose[-1], end='')
print(">")