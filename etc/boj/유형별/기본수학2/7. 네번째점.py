a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())

x = [a,c,e]
y = [b,d,f]
p = 0
q = 0

for i in range(3):
    if x.count(x[i]) == 1:
        p = x[i]
for i in range(3):
    if y.count(y[i]) == 1:
        q = y[i]

print(p, q)