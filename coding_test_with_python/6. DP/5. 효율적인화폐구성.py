# n, m 입력받기
n, m = map(int, input().split())

# 입력값 받아서 내림차순
money = []
for i in range(n):
    a = int(input())
    money.append(a)
money.sort(reverse=True)

# 사용한 화폐의 개수
count = 0

# 계산 알고리즘
for i in money:
    if m % i == 0 and m // i > 0:
        count = count + m // i
        m = m - (m//i) * i
        break
    elif m // i > 0:
        count = count + m // i
        m = m - (m // i) * i

# 돈을 낼수있는 경우에만 count출력
if m != 0:
    print(-1)
else:
    print(count)