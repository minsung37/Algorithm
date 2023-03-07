import sys
input = sys.stdin.readline
n = int(input())

# 자료 담기
b = []
for i in range(n):
    x = sys.stdin.readline()
    y = len(x)
    b.append([y, x])

# list를 tuple로 변환
b1 = list(map(tuple, b))

# tuple을 set으로 변환해 중복값을 제거
b2 = set(list(map(tuple, b1)))
b3 = list(set(b2))
b4 = sorted(b3)

# 정답 출력
for i in range(len(b4)):
    print(b4[i][1], end='')
