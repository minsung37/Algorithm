n = int(input())
a = []
b = []
s = 0
i = 1
j = 0
while True:
    a.append(i)
    i = i + 1
    if i > 4472:
        break
k = len(a)

for i in range(k):
    s = s + a[i]
    b.append(s)

while True:
    if n <= b[j]:
        break
    j = j + 1

total = j + 2
up = b[j] - n + 1
# print(total)
# print(total - up)
if b.index(b[j]) % 2 == 0:
    print(str(up) + "/" + str(total-up))
else:
    print(str(total - up) + "/" + str(up))