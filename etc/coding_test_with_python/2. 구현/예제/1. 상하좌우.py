n = int(input())
x, y = 1, 1
d = input().split()

for i in range(len(d)):
    temp = d[i]
    if temp == "U":
        if x > 1:
            x = x - 1
    elif temp == "D":
        if x < n:
            x = x + 1
    elif temp == "R":
        if y < n:
            y = y + 1
    elif temp == "L":
        if y > 1:
            y = y - 1
print(x,y)