num = list(map(int, input().split()))

check = 0

for i in range(5):
    check = check + num[i] ** 2

print(check % 10)