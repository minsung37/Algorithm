# 조건입력받기
n, k = map(int, (input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a는 오름차순, b는 내림차순
a.sort()
b.sort(reverse=True)
# print(a)
# print(b)

# 교환
for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

# print(a)
print(sum(a))