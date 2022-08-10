# 24 18 => 6 72
n, m = map(int, input().split())

# 최대공약수(The Greatest Common Divisor)
gcd = m
while True:
    if n % gcd == 0 and m % gcd == 0:
        break
    else:
        gcd = gcd - 1
print(gcd)

# 최소공배수(Least Common Multiple)
k = 1
while True:
    lcm = m * k
    if lcm % n == 0:
        break
    else:
        k = k + 1
print(lcm)