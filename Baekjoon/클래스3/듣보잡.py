# 문제조건 입력받기
n, m = map(int, (input().split()))
a = []
b = []
for i in range(n):
    a.append(input())
for i in range(m):
    b.append(input())

# 각 집합의 교집합을 리스트로 변환하여 정렬하기
a = set(a)
b = set(b)
c = a & b
c = list(c)
c.sort()

# 정답 출력
num = len(c)
print(num)
for i in range(num):
    print(c[i])