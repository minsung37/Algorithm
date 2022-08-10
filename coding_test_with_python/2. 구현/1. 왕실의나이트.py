n = input()
x = ord(n[0])-ord("a") + 1
y = int(n[1])
xx = [1,2,2,1,-1,-2,-2,-1]
yy = [2,1,-1,-2,-2,-1,1,2]
res = 0
for i in range(8):
    nx = x + xx[i]
    ny = y + yy[i]
    if 0 < nx < 9 and 0 < ny < 9:
        res = res + 1

print(res)